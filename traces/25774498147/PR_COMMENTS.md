# Added 8 New Fallopian Tube Tissue Layer Terms

## Summary
This PR adds 8 new anatomical terms for the fallopian tube tissue layers, addressing issue #3414. The terms were requested by the Human Cell Atlas team following expert consultation with fallopian tube anatomists at Penn Medicine.

## Background
The initial issue requested terms for mesosalpinx and antimesosalpinx regions and their tissue layers. After consultation with subject matter experts (C. Erik Nordgren, Kate O'Neill, and Stephen Fisher at Penn Medicine), the requirements were clarified in February 2025 to include 8 specific terms representing both mesosalpinx/antimesosalpinx regions and superior/inferior regions.

According to the experts' guidance, these terms describe regional polarity (mesosalpinx, antimesosalpinx, superior, inferior) within the epithelial and muscular layers of the fallopian tube, rather than being separate anatomical structures themselves.

## Terms Added

### Epithelium Terms (all under mucosa of fallopian tube - UBERON:0005048)

1. **UBERON:9900000 - mesosalpinx epithelium**
   - Definition: An epithelium that is part of the mucosa of the fallopian tube and is located in the mesosalpinx region.
   - is_a: epithelium (UBERON:0000483)
   - part_of: mucosa of fallopian tube (UBERON:0005048)

2. **UBERON:9900001 - antimesosalpinx epithelium**
   - Definition: An epithelium that is part of the mucosa of the fallopian tube and is located in the antimesosalpinx region.
   - is_a: epithelium (UBERON:0000483)
   - part_of: mucosa of fallopian tube (UBERON:0005048)

3. **UBERON:9900004 - superior epithelium**
   - Definition: An epithelium that is part of the mucosa of the fallopian tube and is located in the superior region.
   - Synonym: "superior fallopian tube epithelium"
   - is_a: epithelium (UBERON:0000483)
   - part_of: mucosa of fallopian tube (UBERON:0005048)

4. **UBERON:9900005 - inferior epithelium**
   - Definition: An epithelium that is part of the mucosa of the fallopian tube and is located in the inferior region.
   - Synonym: "inferior fallopian tube epithelium"
   - is_a: epithelium (UBERON:0000483)
   - part_of: mucosa of fallopian tube (UBERON:0005048)

### Muscular Layer Terms (all under muscle layer of oviduct - UBERON:0006642)

5. **UBERON:9900002 - mesosalpinx muscularus**
   - Definition: A muscular layer that is part of the muscle layer of the oviduct and is located in the mesosalpinx region.
   - Synonym: "mesosalpinx muscularis"
   - is_a: muscular coat (UBERON:0006660)
   - part_of: muscle layer of oviduct (UBERON:0006642)

6. **UBERON:9900003 - antimesosalpinx muscularus**
   - Definition: A muscular layer that is part of the muscle layer of the oviduct and is located in the antimesosalpinx region.
   - Synonym: "antimesosalpinx muscularis"
   - is_a: muscular coat (UBERON:0006660)
   - part_of: muscle layer of oviduct (UBERON:0006642)

7. **UBERON:9900006 - superior muscularus**
   - Definition: A muscular layer that is part of the muscle layer of the oviduct and is located in the superior region.
   - Synonym: "superior fallopian tube muscularis"
   - is_a: muscular coat (UBERON:0006660)
   - part_of: muscle layer of oviduct (UBERON:0006642)

8. **UBERON:9900007 - inferior muscularus**
   - Definition: A muscular layer that is part of the muscle layer of the oviduct and is located in the inferior region.
   - Synonym: "inferior fallopian tube muscularis"
   - is_a: muscular coat (UBERON:0006660)
   - part_of: muscle layer of oviduct (UBERON:0006642)

## Methodology

1. **Research Phase**: 
   - Reviewed issue context and expert consultation notes from Penn Medicine team
   - Examined existing UBERON terms for fallopian tube anatomy including:
     - mucosa of fallopian tube (UBERON:0005048)
     - muscle layer of oviduct (UBERON:0006642)
     - mesosalpinx (UBERON:0012331)
     - antimesosalpinx (UBERON:8600117)
   - Consulted pathologyoutlines.com for anatomical context

2. **Term Creation**:
   - Used new term IDs starting at UBERON:9900000 as per NTR guidelines
   - Created terms in a batch file (terms/fallopian_tube_batch.obo)
   - Checked terms into main edit file using obo-checkin.pl
   - Reserialized ontology using robot convert

3. **Metadata Applied**:
   - dc-contributor: Ellen Quardokus (ORCID 0000-0001-7655-4833) - original requester
   - term_tracker_item: Links to issue #3414
   - dcterms-date: Current timestamp
   - created_by: dragon-ai-agent

## Validation

- All terms successfully added to src/ontology/uberon-edit.obo
- File properly reserialized using ROBOT
- All terms follow UBERON conventions:
  - Proper genus-differentia definitions
  - Appropriate parent terms based on expert guidance
  - Standard metadata tags

## Notes

- The term "muscularus" is used instead of "muscularis" as specified in the expert communication
- These terms are applicable to both left and right fallopian tubes as noted by the experts
- The mesosalpinx/antimesosalpinx and superior/inferior designations refer to regional polarity within the tissue layers, not separate anatomical structures
- Note: antimesosalpinx (UBERON:8600117) was previously added via issue #3420

## References

- Issue #3414: https://github.com/obophenotype/uberon/issues/3414
- Expert consultation from C. Erik Nordgren, Kate O'Neill, and Stephen Fisher (Penn Medicine), November 26, 2024
- PathologyOutlines.com: Fallopian Tubes Normal Histology

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25774498147)
