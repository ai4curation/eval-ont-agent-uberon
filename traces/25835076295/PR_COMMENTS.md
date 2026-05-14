# Lamina propria terms for GI tract segments (issue #3495)

## Summary

This PR addresses the second half of issue #3495, specifically the
[follow-up request from @dosumis](https://github.com/obophenotype/uberon/issues/3495#issuecomment-2896247830)
to add lamina propria terms for the GI tract segments that didn't yet
have a dedicated lamina propria term. The epithelium half of the issue
was addressed separately in PR #3541.

Seven new terms were created:

| ID | Name | part_of |
| --- | --- | --- |
| UBERON:9900001 | ascending colon lamina propria | UBERON:0001156 (ascending colon) |
| UBERON:9900002 | transverse colon lamina propria | UBERON:0001157 (transverse colon) |
| UBERON:9900003 | descending colon lamina propria | UBERON:0001158 (descending colon) |
| UBERON:9900004 | sigmoid colon lamina propria | UBERON:0001159 (sigmoid colon) |
| UBERON:9900005 | stomach lamina propria | UBERON:0000945 (stomach) |
| UBERON:9900006 | caecum lamina propria | UBERON:0001153 (caecum) |
| UBERON:9900007 | rectum lamina propria | UBERON:0001052 (rectum) |

## Design decisions

- **Genus-differentia logical definition.** Each term has
  `intersection_of: UBERON:0000030 ! lamina propria` and
  `intersection_of: part_of <gut segment>`. Per @dosumis's request,
  there is **no** duplicated `relationship: part_of <gut segment>` —
  the reasoner can infer the part_of from the equivalent class
  definition, exactly as is done for UBERON:8600034 (jejunum lamina
  propria) and UBERON:8600035 (ileum lamina propria).
- **Text definitions** follow the requested pattern: *"The lamina
  propria that underlies the epithelial lining of the {gut segment}."*
- **Naming style** matches the existing UBERON:8600034 / UBERON:8600035
  pattern — `{gut segment} lamina propria` as the primary label with
  `lamina propria of {gut segment}` and adjectival forms (e.g.
  `colonic`, `gastric`, `rectal`) as `EXACT` synonyms.
- **Metadata.** Each term has:
  - `created_by: dragon-ai-agent`
  - `relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland`
    (the requestor)
  - `property_value: dcterms-date "2026-05-14T..." xsd:dateTime`
  - `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3495" xsd:anyURI`
- **ID range.** Used the UBERON:99xxxxx range (UBERON:9900001 …
  UBERON:9900007) as specified in the project's `CLAUDE.md` for new
  term requests. This avoids the UBERON:7770000-7770004 range that
  @dosumis flagged as off-limits in the epithelium ask, and does not
  collide with the in-use UBERON:8600xxx range (latest used:
  UBERON:8600133).
- **Definition xrefs.** Used `ISBN:0123813611` (Treuting & Dintzis,
  *Comparative Anatomy and Histology: A Mouse and Human Atlas*), which
  is already a listed source in the ontology header and covers all the
  GI structures involved. I avoided guessing PMIDs (per the project's
  `CLAUDE.md` rule against guessing PMIDs).

## Checklist

- [x] Read the issue and all four comments
- [x] Verified existing parent terms (UBERON:0000030 lamina propria,
      UBERON:0001156 ascending colon, UBERON:0001157 transverse colon,
      UBERON:0001158 descending colon, UBERON:0001159 sigmoid colon,
      UBERON:0000945 stomach, UBERON:0001153 caecum, UBERON:0001052
      rectum)
- [x] Checked that none of the new term names collide with existing
      terms (only related existing terms found were
      UBERON:0007177 *lamina propria of mucosa of colon*,
      UBERON:0011189 *lamina propria of large intestine*, and
      UBERON:0016511 *lamina propria of fundus of stomach* — these are
      either more specific or grouping classes, so the new
      segment-specific terms are non-redundant)
- [x] Modeled the terms after existing UBERON:8600034 *jejunum lamina
      propria* and UBERON:8600035 *ileum lamina propria*
- [x] Verified no duplicate `relationship: part_of` axioms are
      included (per @dosumis's instruction)
- [x] Added requestor as dc-contributor
- [x] Added term_tracker_item linking back to the issue
- [x] Used edit workflow via `obo-checkout.pl` / `obo-checkin.pl`
- [x] OBO syntax verified (terms successfully checked in via
      `obo-checkin.pl`)

## Notes / open questions

- The issue originally also mentions some *"questions regarding the
  parent terms of existing terms"* — those have not been asked yet in
  the thread, so they are out of scope for this PR.
- The original issue also mentioned `epithelium` terms for colon
  segments. Those were addressed separately in PR #3541 (per
  @cmungall's comments on the issue), so they are intentionally not
  duplicated here.
- I was unable to run `robot convert` to reserialize the edit file
  (robot is not installed in this environment). The new stanzas were
  written in canonical OBO format and the `obo-checkin.pl` round-trip
  succeeded, so the file should be syntactically valid; a reserialize
  pass can be run by a maintainer before merge if desired.

Signed-off-by: @dragon-ai-agent

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25835076295)
