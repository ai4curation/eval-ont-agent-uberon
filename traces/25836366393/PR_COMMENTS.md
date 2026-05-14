# Draft ROBOT template for HuBMAP HRA bone-part terms (issue #3678)

## What's in this PR

Two new files in `src/templates/`:

- `hra_bone_parts.template.tsv` — a ROBOT template covering 129 candidate
  new bone-part terms drawn from the HuBMAP HRA `Uberon_skeleton_terms` CSV
  attached to issue #3678. New terms are assigned IDs in the temporary
  range `UBERON:99XXXXX` (per `uberon-idranges.owl` range 42).
- `hra_bone_parts.report.md` — a data-quality report listing every CSV row
  that was excluded from the template, with the reason.

**`uberon-edit.obo` has NOT been modified.** The template is not wired
into the build (no `Makefile` or catalog entry). It is intended as a
human-reviewable starting point only, not a finished artefact.

## Why this is a draft and not a direct merge

I evaluated the 390 rows in the source CSV against three checks before
deciding what to commit. The numbers came out as:

| Outcome | Rows | Why excluded |
|---|---|---|
| Accepted into draft template | 129 | parent is a bone, parent label is consistent with the term name, term is not an obvious duplicate |
| **Likely duplicate of an existing UBERON term** | 102 | the term name without the trailing `of <bone>` qualifier matches an existing UBERON label or synonym (e.g. `acetabular fossa of os coxa` ≈ `UBERON:0014445 ! acetabular fossa`) |
| **Bad / misaligned parent in CSV** | 159 | `parents_as` column is anatomically incompatible with the term — non-bone parents like muscles, arteries, lymph nodes; or rib-N assigned to rib-M; or the parent ID is an `ASCTB-TEMP` / `FMA` URI rather than a UBERON ID |

A few representative bad-parent rows for context:

- `coronoid fossa of humerus` → `UBERON:0005170 ! granulosa cell layer`
- `costal groove of first rib` → `UBERON:0002512 ! corpus luteum`
- `digastric fossa of mandible` → `ASCTB-TEMP_superior-ulnar-lymph-node`
- `dorsum sellae of sphenoid bone` → `UBERON:0001383 ! muscle of leg`
- `external auditory meatus of squamous part of temporal bone` → `UBERON:0002379 ! perineal muscle`
- `facet of twelfth rib` → `UBERON:0004609 ! rib 10`

These look like a row-level misalignment in the upstream spreadsheet
rather than mistakes Uberon should silently fix; they need to go back to
HuBMAP HRA for re-curation.

## Caveats for review

1. **Definitions are placeholders.** Each accepted row has an
   auto-generated definition of the form *"An anatomical structure that
   is part of a `<parent>`."* This is not a publishable UBERON
   definition. The source CSV cites `https://fipat.library.dal.ca/ta2/`
   (FIPAT *Terminologia Anatomica* 2nd ed.) and `ISBN:9780323393225`
   (Standring, *Gray's Anatomy*) — those should be used to write proper
   genus-differentia definitions before the terms are added to
   `uberon-edit.obo`.

2. **Even the 129 "accepted" rows need a duplicate sweep against existing
   UBERON terms.** My duplicate detector strips the `of <bone>` suffix
   and looks for a name/synonym match, which catches the obvious cases
   but won't catch reformulations (e.g. a new `mandibular angle of
   mandible` row would be caught, but `angle of mandible` versus an
   existing `mandibular angle` requires more semantic matching).

3. **Several of the proposed terms map to design patterns already in use.**
   For example, `vertebral arch of <Nth vertebra>` follows the existing
   pattern of `UBERON:0000218 ! vertebral arch of axis` (`neural arch`
   intersected with `part_of <vertebra>`); `vertebral body of <Nth
   vertebra>` would be a child of `UBERON:0001075 ! bony vertebral
   centrum`; `head of <bone>` follows `UBERON:0006767 ! head of femur`
   (`zone of bone organ` part of the bone); etc. The current draft just
   uses `is_a` + `part_of` to the parent bone — a curator should pick
   the right genus class per row.

4. **Contributor attribution** uses David Osumi-Sutherland's existing
   ORCID (`0000-0002-7073-9172`, the one used elsewhere in
   `uberon-edit.obo`) since he was the one who triaged the issue. This
   should be reviewed if the attribution should go to someone else.

## Self-review checklist

- [x] Did NOT edit `src/ontology/uberon-edit.obo` (data-quality bar not
      met)
- [x] Did NOT wire the template into the build (`Makefile`, catalog,
      imports all unchanged)
- [x] Used the temporary `UBERON:99XXXXX` ID range from
      `src/ontology/uberon-idranges.owl`
- [x] Excluded all rows with non-UBERON parents (FMA / ASCTB-TEMP URIs)
- [x] Excluded all rows whose parent ID is not a known bone
- [x] Excluded all rows whose parent label is anatomically inconsistent
      with the term name
- [x] Cross-checked accepted rows against existing UBERON labels and
      synonyms; flagged 102 likely-duplicate rows in the report
- [x] Confirmed the contributor ORCID is one already used in
      `uberon-edit.obo`
- [x] Only committed the two new files I created

## Suggested next steps for curators

1. Send the bad-parent table back to HuBMAP HRA so they can re-curate the
   `parents_as` column at source.
2. Decide whether the 102 likely-duplicate rows should (a) be dropped
   from the request (with HuBMAP re-mapping its CSV to the existing
   UBERON IDs) or (b) added as exact synonyms on the existing UBERON
   terms.
3. For the 129 accepted rows, write proper definitions from FIPAT TA2 /
   Standring and pick a more specific genus class than the parent bone
   itself (e.g. `bone fossa`, `bony projection`, `neural arch`,
   `vertebral centrum`, etc.). After that, the template can be wired
   into the build by following `src/templates/README.md`.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25836366393)
