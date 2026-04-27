"""
Stage 2: Group ROBOT template rows by parent term for parallel subagent processing.

Reads BOTH templates produced by Stage 1:
  bulk_ntr_workflow/outputs/template_initial.tsv         — leaf terms (SC directives)
  bulk_ntr_workflow/outputs/template_groups_initial.tsv  — group terms (EC directives)

Each per-term JSON entry includes a `term_type` field ("leaf" or "group") so the agent
can branch its behaviour (Step 5 of the agent spec). Group terms have no parent ID
encoded in the template (the agent will determine genus + part_of differentiator), so
they are all collected into a single group keyed by `term_type=group` rather than by
parent UBERON ID.

Output: bulk_ntr_workflow/outputs/definitions/input/{group_name}.json

Usage:
  uv run scripts/group_terms_by_parent.py
"""

import csv
import json
import re
from pathlib import Path

ROOT             = Path(__file__).resolve().parent.parent
INPUT_LEAF_TSV   = ROOT / "outputs" / "template_initial.tsv"
INPUT_GROUPS_TSV = ROOT / "outputs" / "template_groups_initial.tsv"
OUTPUT_DIR       = ROOT / "outputs" / "definitions" / "input"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Leaf template column indices (after the 2 header rows)
# ID | LABEL | Definition | def_xref | is_a | part_of | ...
COL_ID       = 0
COL_LABEL    = 1
COL_DEF      = 2
COL_XREF     = 3
COL_IS_A     = 4
COL_PART_OF  = 5

# Groups template column indices — same first 4, then genus + location
COL_GENUS    = 4
COL_LOCATION = 5


def extract_parent_info(row: list[str]) -> tuple[str, str]:
    """Return (parent_id, parent_label) from a leaf template's is_a/part_of cells."""
    is_a    = row[COL_IS_A].strip()
    part_of = row[COL_PART_OF].strip()

    for val in (is_a, part_of):
        m = re.match(r'^(UBERON:\d{7})$', val)
        if m:
            return m.group(1), ""
        m = re.match(r'^INFER:(UBERON:\d{7})$', val)
        if m:
            return m.group(1), ""
        m = re.match(r'^(NEEDS_MAPPING:FMA:\d+)$', val)
        if m:
            return m.group(1), ""

    val = is_a if is_a and is_a not in ("", "[PENDING]") else part_of
    return val, ""


def make_group_name(parent_id: str, parent_label: str) -> str:
    """Derive a safe filename-friendly group name."""
    if parent_label and parent_label not in ("INFER", "NEEDS_MAPPING", "UNRESOLVABLE", "UNKNOWN"):
        slug = re.sub(r'[^\w]+', '_', parent_label.lower()).strip('_')
        return slug[:50]
    safe = re.sub(r'[^\w]+', '_', parent_id.lower()).strip('_')
    return safe[:50]


def process() -> None:
    if not INPUT_LEAF_TSV.exists():
        raise FileNotFoundError(f"Input not found: {INPUT_LEAF_TSV}\nRun generate_template.py first.")

    groups: dict[str, dict] = {}

    # --- Leaf template: group by parent ---
    with open(INPUT_LEAF_TSV, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)  # header row
        next(reader)  # directive row
        for row in reader:
            if not row or not row[COL_LABEL].strip():
                continue
            label = row[COL_LABEL].strip()
            ntr_id = row[COL_ID].strip()

            parent_id, _ = extract_parent_info(row)
            group_key = parent_id

            if group_key not in groups:
                groups[group_key] = {
                    "parent_id":   parent_id,
                    "parent_label": "",
                    "terms":       [],
                }

            groups[group_key]["terms"].append({
                "ntr_id":     ntr_id,
                "label":      label,
                "term_type":  "leaf",
                "is_a":       row[COL_IS_A].strip(),
                "part_of":    row[COL_PART_OF].strip(),
                "def_xref":   row[COL_XREF].strip() if len(row) > COL_XREF else "",
            })

    # --- Groups template: all into one bucket; agent determines genus + location per term ---
    if INPUT_GROUPS_TSV.exists():
        with open(INPUT_GROUPS_TSV, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)  # header row
            next(reader)  # directive row
            grouping_terms = []
            for row in reader:
                if not row or not row[COL_LABEL].strip():
                    continue
                grouping_terms.append({
                    "ntr_id":     row[COL_ID].strip(),
                    "label":      row[COL_LABEL].strip(),
                    "term_type":  "group",
                    "genus":      row[COL_GENUS].strip() if len(row) > COL_GENUS else "",
                    "location":   row[COL_LOCATION].strip() if len(row) > COL_LOCATION else "",
                    "def_xref":   row[COL_XREF].strip() if len(row) > COL_XREF else "",
                })
            if grouping_terms:
                groups["__grouping_terms__"] = {
                    "parent_id":    "GROUPING_TERMS",
                    "parent_label": "(grouping terms — agent determines genus + part_of differentiator per term)",
                    "terms":        grouping_terms,
                }

    written = 0
    for group_key, data in sorted(groups.items()):
        parent_id = data["parent_id"]
        # Special handling for the grouping bucket
        if group_key == "__grouping_terms__":
            group_name = "grouping_terms"
        else:
            group_name = make_group_name(parent_id, data.get("parent_label", ""))

        # Group-level summary: leaf vs group counts (always one or the other in this iteration)
        leaf_n  = sum(1 for t in data["terms"] if t.get("term_type") == "leaf")
        group_n = sum(1 for t in data["terms"] if t.get("term_type") == "group")

        out = {
            "group_name":    group_name,
            "parent_id":     parent_id,
            "parent_label":  data.get("parent_label", ""),
            "term_counts":   {"leaf": leaf_n, "group": group_n},
            "note": "parent_label is best-effort; subagent should resolve via OLS4. "
                    "For term_type='group' terms: use obo-grep on uberon-edit.obo to find "
                    "similar UBERON groupings, identify the genus + part_of pattern, and "
                    "fill genus + location. If pattern doesn't fit, route to manual_curation.",
            "terms":         data["terms"],
        }

        out_path = OUTPUT_DIR / f"{group_name}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)

        marker = "[GROUP]" if group_n else "[leaf] "
        print(f"  {marker} {group_name:45s}  {len(data['terms']):3d} terms")
        written += 1

    total = sum(len(d["terms"]) for d in groups.values())
    print(f"\nTotal groups: {written}  |  Total terms: {total}")


if __name__ == "__main__":
    process()
