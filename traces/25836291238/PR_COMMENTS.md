# Add 5 new HRA terms (issue #3657)

Adds the five HRA/HuBMAP terms agreed upon in [issue #3657](https://github.com/obophenotype/uberon/issues/3657) after iterative clarification with the requester (@zhengj2007).

## Terms added

| ID | Label | is_a | part_of |
|----|-------|------|---------|
| `UBERON:1200004` | salivary gland ducto-acinar unit | `UBERON:0009911` lobule | `UBERON:0001044` saliva-secreting gland |
| `UBERON:1200005` | parotid gland ducto-acinar unit | `UBERON:1200004` salivary gland ducto-acinar unit | `UBERON:0001831` parotid gland |
| `UBERON:1200006` | sublingual gland ducto-acinar unit | `UBERON:1200004` salivary gland ducto-acinar unit | `UBERON:0001832` sublingual gland |
| `UBERON:1200007` | submandibular gland ducto-acinar unit | `UBERON:1200004` salivary gland ducto-acinar unit | `UBERON:0001736` submandibular gland |
| `UBERON:1200008` | dentogingival junction | `UBERON:0000481` multi-tissue structure | `UBERON:0001828` gingiva |

## Rationale

### Salivary gland ducto-acinar units (UBERON:1200004–1200007)
The requested concept is the "ducto-acinar" FTU (functional tissue unit), also called the **salivon** in classical salivary physiology. Per the requester, this is the integrated acinar + ductal module *plus* its associated stromal/vascular microenvironment — explicitly **not** restricted to epithelium alone, and not a transitional interface or transcriptomic cell population.

This was modeled analogously to **lobule of mammary gland** (`UBERON:0001912`), which is `is_a` `lobule` (`UBERON:0009911`) and is `part_of` the mammary gland. The same pattern fits the salivary ducto-acinar unit: a repeating lobule-scale structural-functional module of a salivary gland. The three gland-specific terms are subclasses of the generic parent, differentiated by acinar composition (serous / mucous / mixed).

The requested label "ducto-acinar" was promoted to "ducto-acinar unit" for ontological clarity (this is an anatomical structure, not an adjective). The shorter form is preserved as a RELATED synonym for HRA annotation, and "salivon" is added as an EXACT synonym on the parent.

### Dentogingival junction (UBERON:1200008)
The requested label was "gingival attachment", but the requester confirmed the intent is **the entire dentogingival/periodontal attachment apparatus** — a multi-tissue complex (junctional epithelium + supracrestal connective tissue attachment + stromal/vascular elements), not gingival epithelium alone.

Existing UBERON terms reviewed:
- `UBERON:0035149` gingival epithelial attachment — only the epithelial junction; too narrow.
- `UBERON:0001949` gingival epithelium — epithelial layer of the gingiva; too narrow.
- `UBERON:0001758` periodontium — full tooth-supporting apparatus including PDL/cementum/alveolar bone; too broad.

None of these cover the requested multi-tissue attachment complex, so a new term was added.

- **Preferred label:** `dentogingival junction` — the standard anatomical term in Ten Cate's Oral Histology and Schroeder's *The Periodontium*; avoids the ambiguity of "gingival attachment" (which different sources use to mean attached gingiva, junctional epithelium, or the supracrestal tissue attachment).
- **Synonym (RELATED):** `gingival attachment` — preserved so HRA annotation against the requested label still resolves.
- **Synonym (RELATED):** `dentogingival complex`, `supracrestal tissue attachment` — additional aliases used in the literature.
- **is_a:** `UBERON:0000481` multi-tissue structure — accurate given the explicitly multi-tissue scope (corrected from the proposal's `tissue`, since by UBERON's definitions "tissue" is restricted to one or a few cell types in a single extracellular matrix arrangement; a complex of distinct epithelial + connective + vascular tissues is a multi-tissue structure).
- **part_of:** `UBERON:0001828` gingiva — as requested.

## Metadata added on each term
- `relationship: dc-contributor https://orcid.org/0000-0002-2999-0103` (issue requester ORCID)
- `property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime`
- `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3657"`
- `created_by: dragon-ai-agent`
- `subset: added_by_HRA`
- Gland-specific ducto-acinar terms and the dentogingival junction also carry the HuBMAP dataset DOI as an `xref`.

## Validation checklist
- [x] Parent terms verified to exist (`UBERON:0009911`, `UBERON:0001044`, `UBERON:0001831`, `UBERON:0001832`, `UBERON:0001736`, `UBERON:0000481`, `UBERON:0001828`).
- [x] Existing related terms reviewed for overlap (`UBERON:0001912` mammary gland lobule used as design template; `UBERON:0035149`, `UBERON:0001949`, `UBERON:0001758` reviewed to confirm `dentogingival junction` does not duplicate them).
- [x] Each new term has a definition with definition xrefs, a single textual definition mirrored by the logical parent, an `is_a` parent, and required UBERON contributor / date / tracker metadata.
- [x] Term tracker item points back to issue #3657.
- [x] All terms tagged with the `added_by_HRA` subset.
- [x] Batch checked in via `obo-checkin.pl`; `terms/` cleared after check-in.
- [ ] Reserialisation via `robot convert` was not run — `robot` is not available in this environment. The file was edited via `obo-checkin.pl`, which preserves OBO syntax; please run `make` / `robot convert` locally before release if normalised serialisation is needed.

## Notes for reviewers
- Taxon scope: the requester noted these terms are intended for **human** anatomy (HRA spatial anchoring). I did **not** add an `in_taxon NCBITaxon:9606` constraint, to keep the terms reusable across mammalian species where the underlying anatomy is comparable. Happy to add the taxon constraint if reviewers prefer.
- Stromal/vascular components are described in the textual definitions but not encoded as `has_part` axioms, since at this level of generality the more specific tissue/cell parts vary across the three gland-specific instances.
- PMID:38876998 (the originally cited paper for the gingival term) is retained as a definition xref on `dentogingival junction` per the agreed proposal, alongside ISBN:9780323096300 (Ten Cate's Oral Histology) which is the primary anatomical reference for this concept.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25836291238)
