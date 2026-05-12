# PR Description: Issue #3657 - New UBERON Terms for HRA/HuBMAP

## Summary

This PR adds five new terms to the UBERON ontology requested by HRA/HuBMAP for spatial annotation of functional tissue units (FTUs) in human salivary glands and periodontal tissues. The terms follow established UBERON design patterns and design principles.

## Terms Added

### 1. Salivary Gland Ducto-Acinar Unit (UBERON:9900001)
**Parent:** UBERON:0009911 (lobule)  
**Relationships:** part_of UBERON:0001044 (saliva-secreting gland)  
**Definition:** A lobule of a salivary gland consisting of secretory acini together with their contiguous ductal segments (intercalated and striated ducts), myoepithelial cells, stromal tissue, and vasculature.  
**Synonyms:** "salivon" (EXACT), "salivary gland ducto-acinar" (RELATED)  
**Rationale:** This is a generic parent term representing the functional tissue unit (FTU) concept from HRA—the repeating structural-functional modules that integrate epithelial, stromal, and vascular compartments. Modeled after mammary gland lobule (UBERON:0001912) for consistency.

### 2. Parotid Gland Ducto-Acinar Unit (UBERON:9900002)
**Parent:** UBERON:9900001 (salivary gland ducto-acinar unit)  
**Relationships:** part_of UBERON:0001831 (parotid gland)  
**Definition:** Gland-specific variant consisting of purely serous acini with contiguous ductal segments and associated myoepithelial cells, stromal tissue, and vasculature. Produces watery, protein-rich serous saliva.

### 3. Sublingual Gland Ducto-Acinar Unit (UBERON:9900003)
**Parent:** UBERON:9900001 (salivary gland ducto-acinar unit)  
**Relationships:** part_of UBERON:0001832 (sublingual gland)  
**Definition:** Gland-specific variant consisting of predominantly mucous acini (with minor serous demilunes) and associated ductal segments, myoepithelial cells, stromal tissue, and vasculature. Produces viscous, mucin-rich saliva.

### 4. Submandibular Gland Ducto-Acinar Unit (UBERON:9900004)
**Parent:** UBERON:9900001 (salivary gland ducto-acinar unit)  
**Relationships:** part_of UBERON:0001736 (submandibular gland)  
**Definition:** Gland-specific variant consisting of mixed acini (approximately 90% serous, 10% mucous) and associated ductal segments, myoepithelial cells, stromal tissue, and vasculature. Produces mixed serous-mucous saliva.

### 5. Dentogingival Junction (UBERON:9900005)
**Parent:** UBERON:0000479 (tissue)  
**Relationships:** part_of UBERON:0001828 (gingiva)  
**Definition:** Multi-tissue anatomical complex constituting the attachment zone between gingival tissue and tooth surface. Comprises junctional epithelium, supracrestal connective tissue attachment fibers, and supporting stromal and vascular elements.  
**Synonyms:** "gingival attachment" (RELATED), "dentogingival complex" (RELATED), "supracrestal tissue attachment" (RELATED)  
**Rationale:** Fills a gap in UBERON by providing a term for the entire dentogingival attachment apparatus (not just the epithelial component, which is already captured by UBERON:0035149). Distinct from the broader periodontium (UBERON:0001758).

## Design Decisions

1. **Ducto-Acinar Terms as Lobules:** Following the precedent of UBERON:0001912 (mammary gland lobule), the ducto-acinar unit was modeled as `is_a UBERON:0009911 (lobule)`. This reflects the concept of a repeating structural-functional module within a gland, consistent with HRA's FTU definition.

2. **Multi-Tissue Representation:** Unlike simpler anatomical terms, these FTUs explicitly represent the integration of epithelial, stromal, and vascular components in their definitions, reflecting the multicellular nature of functional tissue units.

3. **Gland-Specific Variants:** The three gland-specific ducto-acinar terms differ in acinar cell composition (serous vs. mucous vs. mixed), accurately reflecting histological differences between parotid, sublingual, and submandibular glands.

4. **Label Choice for Dentogingival Term:** "Dentogingival junction" was chosen as the preferred label (with "gingival attachment" as a RELATED synonym) to:
   - Match standard anatomical terminology (Ten Cate's Oral Histology)
   - Avoid ambiguity (the literature uses "gingival attachment" inconsistently)
   - Clearly distinguish from UBERON:0035149 (gingival epithelial attachment, epithelial component only)

## Metadata and Attribution

- All terms include proper attributions (dc-contributor: ORCID:0000-0002-2999-0103)
- All terms include creation dates (dcterms-date)
- All terms include taxon constraints (in_taxon: NCBITaxon:9606) as these are human-specific anatomical terms
- All terms include cross-reference to HubMAP dataset (xref: https://doi.org/10.48539/HBM632.GTVR.643)
- References include peer-reviewed literature (PMID:24862590) and standard anatomical textbooks (ISBN:9780323096300)

## Validation

- All parent terms (UBERON:0009911, UBERON:0001044, UBERON:0001831, UBERON:0001832, UBERON:0001736, UBERON:0000479, UBERON:0001828) exist and are appropriate
- No logical errors in term definitions or relationships
- All terms follow OBO Format conventions
- Metadata follows UBERON standards with proper attribution to the requesting party

## References Cited

- PMID:24862590 (Holmberg & Hoffman 2014 - Salivary gland anatomy and biogenesis)
- https://www.ncbi.nlm.nih.gov/books/NBK538325/ (StatPearls: Anatomy, Salivary Glands)
- ISBN:9780323096300 (Ten Cate's Oral Histology, 8th ed. - Dentogingival junction anatomy)
- https://doi.org/10.48539/HBM632.GTVR.643 (HubMAP dataset)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/uberon-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-uberon/actions/runs/25762022282)
