# HuBMAP HRA bone-part terms — data quality report

Source: GitHub issue [#3678](https://github.com/obophenotype/uberon/issues/3678) (file `Uberon_skeleton_terms - Sheet1.csv`).

- Total rows in source CSV: **390**
- Rows in draft ROBOT template: **129**
- Rows likely already in UBERON (excluded): **102**
- Rows with bad/misaligned parent (excluded): **159**

## Important caveats

1. **The draft ROBOT template has NOT been wired into the build** and **no terms have been added to `uberon-edit.obo`**. The template lives in `src/templates/hra_bone_parts.template.tsv` for human review.

2. **Definitions are placeholders.** Each definition is auto-generated as `"An anatomical structure that is part of a <parent>."` This is not a publishable UBERON definition; the FIPAT TA2 / Standring textbook references provided by the issue should be used to write proper genus-differentia definitions.

3. **Many terms in the source CSV are duplicates** of existing UBERON terms with shorter names (e.g. `acetabular fossa of os coxa` ≈ `UBERON:0014445 ! acetabular fossa`). The `Likely duplicates` section below lists these — they should be reviewed manually and either re-mapped to existing UBERON IDs in the HuBMAP CSV or added as exact synonyms on the existing terms.

4. **The source CSV has many corrupted parent assignments.** About 40% of rows have a `parents_as` column whose ID/label is anatomically incompatible with the term name (e.g. `coronoid fossa of humerus` → `UBERON:0005170 ! granulosa cell layer`). These rows are listed in the `Bad parent` section and need to be re-curated at source by HuBMAP HRA before they can be added.

## Bad parent (excluded from template)

| Term name | Proposed parent ID | Proposed parent label | Reason |
|---|---|---|---|
| coronoid fossa of humerus | `UBERON:0005170` | granulosa cell layer | parent UBERON:0005170 (granulosa cell layer) is not a bone |
| costal groove of first rib | `UBERON:0002512` | corpus luteum | parent UBERON:0002512 (corpus luteum) is not a bone |
| costal groove of twelfth rib | `UBERON:0004601` | rib 1 | term name does not match parent label 'rib 1' (likely misaligned) |
| costal notches of sternum | `UBERON:0004611` | rib 12 | term name does not match parent label 'rib 12' (likely misaligned) |
| costal region bone | `https://purl.org/ccf/ASCTB-TEMP_respiratory-diaphragm-muscle` | respiratory diaphragm muscle | parent ID is not a UBERON identifier |
| cribiform plate of ethmoid bone | `UBERON:0014477` | thoracic skeleton | term name does not match parent label 'thoracic skeleton' (likely misaligned) |
| digastric fossa of mandible | `https://purl.org/ccf/ASCTB-TEMP_superior-ulnar-lymph-node` | superior ulnar lymph node | parent ID is not a UBERON identifier |
| dorsum sellae of sphenoid bone | `UBERON:0001383` | muscle of leg | parent UBERON:0001383 (muscle of leg) is not a bone |
| ethmoidal air cells of ethmoid bone | `http://purl.org/sig/ont/fma/fma234924` | Brachial lymphatic vessel | parent ID is not a UBERON identifier |
| external auditory meatus of squamous part of temporal bone | `UBERON:0002379` | perineal muscle | parent UBERON:0002379 (perineal muscle) is not a bone |
| external occipital protuberance of squamous part of occipital bone | `UBERON:0002376` | cranial muscle | parent UBERON:0002376 (cranial muscle) is not a bone |
| facet of eleventh rib | `UBERON:0035404` | superior hypophysial artery | parent UBERON:0035404 (superior hypophysial artery) is not a bone |
| facet of first rib | `UBERON:0004610` | rib 11 | term name does not match parent label 'rib 11' (likely misaligned) |
| facet of tenth rib | `UBERON:0004601` | rib 1 | term name does not match parent label 'rib 1' (likely misaligned) |
| facet of twelfth rib | `UBERON:0004609` | rib 10 | term name does not match parent label 'rib 10' (likely misaligned) |
| fibular facet of tibia | `UBERON:0004611` | rib 12 | term name does not match parent label 'rib 12' (likely misaligned) |
| fibular trochlea of calcaneus | `UBERON:0000979` | tibia | term name does not match parent label 'tibia' (likely misaligned) |
| foramen lacerum of sphenoid bone | `http://purl.org/sig/ont/fma/fma43942` | Plantar arch | parent ID is not a UBERON identifier |
| foramen magnum of basilar part of occipital bone | `UBERON:0001677` | sphenoid bone | term name does not match parent label 'sphenoid bone' (likely misaligned) |
| foramen ovale of sphenoid bone | `UBERON:0001676` | occipital bone | term name does not match parent label 'occipital bone' (likely misaligned) |
| fossa for lacrimal sac of lacrimal bone | `UBERON:0001677` | sphenoid bone | term name does not match parent label 'sphenoid bone' (likely misaligned) |
| free part of arm bone | `UBERON:0012419` | taenia coli | parent UBERON:0012419 (taenia coli) is not a bone |
| free part of leg bone | `UBERON:0003460` | arm bone | term name does not match parent label 'arm bone' (likely misaligned) |
| frontal crest of frontal bone | `UBERON:0010946` | occipitofrontalis muscle | parent UBERON:0010946 (occipitofrontalis muscle) is not a bone |
| glabella of frontal bone | `UBERON:0001828` | gingiva | parent UBERON:0001828 (gingiva) is not a bone |
| glenoid fossa of scapula | `UBERON:0000209` | tetrapod frontal bone | term name does not match parent label 'tetrapod frontal bone' (likely misaligned) |
| gluteal surface of ilium of os coxa | `UBERON:0006849` | scapula | term name does not match parent label 'scapula' (likely misaligned) |
| gluteal tuberosity of femur | `UBERON:0001272` | innominate bone | term name does not match parent label 'innominate bone' (likely misaligned) |
| granula foveaolae of parietal bone | `UBERON:0000981` | femur | term name does not match parent label 'femur' (likely misaligned) |
| greater cornu of hyoid bone | `UBERON:0000210` | tetrapod parietal bone | term name does not match parent label 'tetrapod parietal bone' (likely misaligned) |
| greater palatine canal of maxilla | `UBERON:0001685` | hyoid bone | term name does not match parent label 'hyoid bone' (likely misaligned) |
| greater palatine foramen of palatine bone | `UBERON:0002397` | maxilla | term name does not match parent label 'maxilla' (likely misaligned) |
| greater sciatic notch of ilium of os coxa | `UBERON:0001682` | palatine bone | term name does not match parent label 'palatine bone' (likely misaligned) |
| greater wings of sphenoid bone | `UBERON:0001272` | innominate bone | term name does not match parent label 'innominate bone' (likely misaligned) |
| groove for fibularis longus tendon of cuboid | `UBERON:0001677` | sphenoid bone | term name does not match parent label 'sphenoid bone' (likely misaligned) |
| groove for middle meningeal a. of parietal bone | `UBERON:0001455` | cuboid bone | term name does not match parent label 'cuboid bone' (likely misaligned) |
| groove for nasopalatine nerve of vomer | `UBERON:0000210` | tetrapod parietal bone | term name does not match parent label 'tetrapod parietal bone' (likely misaligned) |
| groove for posterior deep temporal artery of squamous part of temporal bone | `UBERON:0002396` | vomer | term name does not match parent label 'vomer' (likely misaligned) |
| groove for subclavian artery of first rib | `UBERON:0001678` | temporal bone | term name does not match parent label 'temporal bone' (likely misaligned) |
| groove for superior sagittal sinus of frontal bone | `UBERON:0004601` | rib 1 | term name does not match parent label 'rib 1' (likely misaligned) |
| groove for superior sagittal sinus of parietal bone | `UBERON:0000209` | tetrapod frontal bone | term name does not match parent label 'tetrapod frontal bone' (likely misaligned) |
| groove for tendon of flexor hallucis longus muscle of calcaneus | `UBERON:0000210` | tetrapod parietal bone | term name does not match parent label 'tetrapod parietal bone' (likely misaligned) |
| groove for transverse sinus of squamous part of occipital bone | `UBERON:0001450` | calcaneus | term name does not match parent label 'calcaneus' (likely misaligned) |
| groove for vertebral artery of first cervical vertebra | `UBERON:0001676` | occipital bone | term name does not match parent label 'occipital bone' (likely misaligned) |
| head of radius of radius | `UBERON:0000370` | adductor magnus | parent UBERON:0000370 (adductor magnus) is not a bone |
| head of second distal phalanx of foot | `UBERON:0001423` | radius bone | term name does not match parent label 'radius bone' (likely misaligned) |
| head of second distal phalanx of hand | `UBERON:0004316` | distal phalanx of pedal digit 2 | term name does not match parent label 'distal phalanx of pedal digit 2' (likely misaligned) |
| head of second middle phalanx of foot | `UBERON:0004311` | distal phalanx of manual digit 2 | term name does not match parent label 'distal phalanx of manual digit 2' (likely misaligned) |
| head of second middle phalanx of hand | `UBERON:0004324` | middle phalanx of pedal digit 2 | term name does not match parent label 'middle phalanx of pedal digit 2' (likely misaligned) |
| head of third middle phalanx of hand | `UBERON:0004320` | middle phalanx of manual digit 2 | term name does not match parent label 'middle phalanx of manual digit 2' (likely misaligned) |
| head of ulna of ulna | `UBERON:0004321` | middle phalanx of manual digit 3 | term name does not match parent label 'middle phalanx of manual digit 3' (likely misaligned) |
| hiatus and groove of petrous part of temporal bone for greater petrosal nerve | `https://purl.org/ccf/ASCTB-TEMP_segmental-hepatic-artery` | segmental hepatic artery | parent ID is not a UBERON identifier |
| hyoid region bone | `http://purl.org/sig/ont/fma/fma8616` | Trunk of right upper lobar artery | parent ID is not a UBERON identifier |
| hypoglossal canal of basilar part of occipital bone | `https://purl.org/ccf/ASCTB-TEMP_neuromeningeal-trunk` | neuromeningeal trunk | parent ID is not a UBERON identifier |
| hypophyseal fossa of sphenoid bone | `UBERON:0001676` | occipital bone | term name does not match parent label 'occipital bone' (likely misaligned) |
| iliac crest of ilium of os coxa | `UBERON:0001499` | muscle of arm | parent UBERON:0001499 (muscle of arm) is not a bone |
| iliopubic ramus of os coxa | `http://purl.org/sig/ont/fma/fma71302` | Erector spinae muscle group | parent ID is not a UBERON identifier |
| incisive foramen of maxilla | `UBERON:0001272` | innominate bone | term name does not match parent label 'innominate bone' (likely misaligned) |
| inferior articular facet of eighth thoracic vertebra | `UBERON:0014685` | pterygoid plexus | parent UBERON:0014685 (pterygoid plexus) is not a bone |
| inferior articular facet of eleventh thoracic vertebra | `UBERON:0011050` | thoracic vertebra 8 | term name does not match parent label 'thoracic vertebra 8' (likely misaligned) |
| inferior articular facet of fifth cervical vertebra | `UBERON:0004635` | thoracic vertebra 11 | term name does not match parent label 'thoracic vertebra 11' (likely misaligned) |
| inferior articular facet of fifth thoracic vertebra | `UBERON:0004614` | mammalian cervical vertebra 5 | term name does not match parent label 'mammalian cervical vertebra 5' (likely misaligned) |
| inferior articular facet of first cervical vertebra | `UBERON:0004630` | thoracic vertebra 5 | term name does not match parent label 'thoracic vertebra 5' (likely misaligned) |
| inferior articular facet of first thoracic vertebra | `UBERON:0001092` | vertebral bone 1 | term name does not match parent label 'vertebral bone 1' (likely misaligned) |
| inferior articular facet of fourth cervical vertebra | `UBERON:0004626` | thoracic vertebra 1 | term name does not match parent label 'thoracic vertebra 1' (likely misaligned) |
| inferior articular facet of fourth thoracic vertebra | `UBERON:0004613` | mammalian cervical vertebra 4 | term name does not match parent label 'mammalian cervical vertebra 4' (likely misaligned) |
| inferior articular facet of ninth thoracic vertebra | `UBERON:0004629` | thoracic vertebra 4 | term name does not match parent label 'thoracic vertebra 4' (likely misaligned) |
| inferior articular facet of second cervical vertebra | `UBERON:0004633` | thoracic vertebra 9 | term name does not match parent label 'thoracic vertebra 9' (likely misaligned) |
| inferior articular facet of second thoracic vertebra | `UBERON:0001093` | vertebral bone 2 | term name does not match parent label 'vertebral bone 2' (likely misaligned) |
| inferior articular facet of seventh cervical vertebra | `UBERON:0004627` | thoracic vertebra 2 | term name does not match parent label 'thoracic vertebra 2' (likely misaligned) |
| inferior articular facet of seventh thoracic vertebra | `UBERON:0004616` | mammalian cervical vertebra 7 | term name does not match parent label 'mammalian cervical vertebra 7' (likely misaligned) |
| inferior articular facet of sixth cervical vertebra | `UBERON:0004632` | thoracic vertebra 7 | term name does not match parent label 'thoracic vertebra 7' (likely misaligned) |
| inferior articular facet of sixth thoracic vertebra | `UBERON:0004615` | mammalian cervical vertebra 6 | term name does not match parent label 'mammalian cervical vertebra 6' (likely misaligned) |
| inferior articular facet of tenth thoracic vertebra | `UBERON:0004631` | thoracic vertebra 6 | term name does not match parent label 'thoracic vertebra 6' (likely misaligned) |
| inferior articular facet of third cervical vertebra | `UBERON:0004634` | thoracic vertebra 10 | term name does not match parent label 'thoracic vertebra 10' (likely misaligned) |
| inferior articular facet of third thoracic vertebra | `UBERON:0004612` | mammalian cervical vertebra 3 | term name does not match parent label 'mammalian cervical vertebra 3' (likely misaligned) |
| inferior articular facet of twelfth thoracic vertebra | `UBERON:0004628` | thoracic vertebra 3 | term name does not match parent label 'thoracic vertebra 3' (likely misaligned) |
| inferior articular process of first cervical vertebra | `UBERON:0004636` | thoracic vertebra 12 | term name does not match parent label 'thoracic vertebra 12' (likely misaligned) |
| inferior articular process of second cervical vertebra | `UBERON:0001092` | vertebral bone 1 | term name does not match parent label 'vertebral bone 1' (likely misaligned) |
| inferior costal facet of eleventh thoracic vertebra | `UBERON:0001093` | vertebral bone 2 | term name does not match parent label 'vertebral bone 2' (likely misaligned) |
| inferior costal facet of tenth thoracic vertebra | `UBERON:0004635` | thoracic vertebra 11 | term name does not match parent label 'thoracic vertebra 11' (likely misaligned) |
| inferior mental spine of mandible | `UBERON:0001576` | intrinsic muscle of tongue | parent UBERON:0001576 (intrinsic muscle of tongue) is not a bone |
| inferior nuchal line of squamous part of occipital bone | `UBERON:0001684` | mandible | term name does not match parent label 'mandible' (likely misaligned) |
| inferior pubic ramus of pubis of os coxa | `https://purl.org/ccf/ASCTB-TEMP_pharyngeal-trunk` | pharyngeal trunk | parent ID is not a UBERON identifier |
| inferior vertebral notch of first cervical vertebra | `UBERON:0001639` | hepatic portal vein | parent UBERON:0001639 (hepatic portal vein) is not a bone |
| infraglenoid tubercle of scapula | `UBERON:0001092` | vertebral bone 1 | term name does not match parent label 'vertebral bone 1' (likely misaligned) |
| infraorbital canal of maxilla | `UBERON:0006849` | scapula | term name does not match parent label 'scapula' (likely misaligned) |
| infraspinous fossa of scapula | `UBERON:0014685` | pterygoid plexus | parent UBERON:0014685 (pterygoid plexus) is not a bone |
| intercondylar notch of femur | `https://purl.org/ccf/ASCTB-TEMP_submandibular-gland-ducto-acinar` | submandibular gland ducto-acinar | parent ID is not a UBERON identifier |
| intermaxillary suture of maxilla | `http://purl.org/sig/ont/fma/fma70929` | Set of pancreatic veins | parent ID is not a UBERON identifier |
| intermediate sacral crest of sacrum | `UBERON:0002324` | muscle of back | parent UBERON:0002324 (muscle of back) is not a bone |
| internal auditory meatus of petrous part of temporal bone | `UBERON:0002461` | anterior abdominal wall muscle | parent UBERON:0002461 (anterior abdominal wall muscle) is not a bone |
| internal occipital protuberance of squamous part of occipital bone | `UBERON:0001678` | temporal bone | term name does not match parent label 'temporal bone' (likely misaligned) |
| interosseus border of tibia | `https://purl.org/ccf/ASCTB-TEMP_external-primary-capillary-plexus-of-median-eminence` | external primary capillary plexus of median eminence | parent ID is not a UBERON identifier |
| ischial body of ischium of os coxa | `UBERON:0002376` | cranial muscle | parent UBERON:0002376 (cranial muscle) is not a bone |
| jugular foramen of basilar part of occipital bone | `https://purl.org/ccf/ASCTB-TEMP_neuromeningeal-trunk` | neuromeningeal trunk | parent ID is not a UBERON identifier |
| jugular foramen of petrous part of temporal bone | `UBERON:0001676` | occipital bone | term name does not match parent label 'occipital bone' (likely misaligned) |
| lacrimal fossa of frontal bone | `UBERON:0001678` | temporal bone | term name does not match parent label 'temporal bone' (likely misaligned) |
| lamina of first cervical vertebra | `UBERON:0000209` | tetrapod frontal bone | term name does not match parent label 'tetrapod frontal bone' (likely misaligned) |
| lamina of second cervical vertebra | `UBERON:0001092` | vertebral bone 1 | term name does not match parent label 'vertebral bone 1' (likely misaligned) |
| lateral process of tuberosity of calcaneus | `https://purl.org/ccf/ASCTB-TEMP_segmental-back-muscle` | segmental back muscle | parent ID is not a UBERON identifier |
| lateral pterygoid plate of sphenoid bone | `https://purl.org/ccf/ASCTB-TEMP_third-common-plantar-digital-artery` | third common plantar digital artery | parent ID is not a UBERON identifier |
| lateral sacral crest of sacrum | `UBERON:0001677` | sphenoid bone | term name does not match parent label 'sphenoid bone' (likely misaligned) |
| lesser cornu of hyoid bone | `https://purl.org/ccf/ASCTB-TEMP_left-anterior-mediastinal-lymph-node` | left anterior mediastinal lymph node | parent ID is not a UBERON identifier |
| lesser palatine foramen of palatine bone | `UBERON:0001685` | hyoid bone | term name does not match parent label 'hyoid bone' (likely misaligned) |
| lesser sciatic notch of ischium of os coxa | `UBERON:0001682` | palatine bone | term name does not match parent label 'palatine bone' (likely misaligned) |
| lesser wings of sphenoid bone | `UBERON:0001272` | innominate bone | term name does not match parent label 'innominate bone' (likely misaligned) |
| linea terminalis of sacrum | `https://purl.org/ccf/ASCTB-TEMP_levator-costarum-muscle` | levator costarum muscle | parent ID is not a UBERON identifier |
| lunate surface of os coxa | `https://purl.org/ccf/ASCTB-TEMP_anterior-vertebral-muscle` | anterior vertebral muscle | parent ID is not a UBERON identifier |
| non-articular facet of tubercle of eighth rib | `UBERON:0004601` | rib 1 | term name does not match parent label 'rib 1' (likely misaligned) |
| non-articular facet of tubercle of fifth rib | `UBERON:0004604` | rib 4 | term name does not match parent label 'rib 4' (likely misaligned) |
| non-articular facet of tubercle of first rib | `UBERON:0004608` | rib 9 | term name does not match parent label 'rib 9' (likely misaligned) |
| non-articular facet of tubercle of fourth rib | `UBERON:0004602` | rib 2 | term name does not match parent label 'rib 2' (likely misaligned) |
| non-articular facet of tubercle of ninth rib | `UBERON:0004607` | rib 7 | term name does not match parent label 'rib 7' (likely misaligned) |
| non-articular facet of tubercle of second rib | `UBERON:0004606` | rib 6 | term name does not match parent label 'rib 6' (likely misaligned) |
| non-articular facet of tubercle of seventh rib | `UBERON:0004609` | rib 10 | term name does not match parent label 'rib 10' (likely misaligned) |
| non-articular facet of tubercle of sixth rib | `UBERON:0004603` | rib 3 | term name does not match parent label 'rib 3' (likely misaligned) |
| non-articular facet of tubercle of tenth rib | `UBERON:0010401` | spleen central arteriole | parent UBERON:0010401 (spleen central arteriole) is not a bone |
| non-articular facet of tubercle of third rib | `UBERON:0001272` | innominate bone | term name does not match parent label 'innominate bone' (likely misaligned) |
| obturator foramen of os coxa | `UBERON:0010946` | occipitofrontalis muscle | parent UBERON:0010946 (occipitofrontalis muscle) is not a bone |
| obturator groove of pubis of os coxa | `UBERON:0001676` | occipital bone | term name does not match parent label 'occipital bone' (likely misaligned) |
| occipital condyle of basilar part of occipital bone | `UBERON:0000976` | humerus | term name does not match parent label 'humerus' (likely misaligned) |
| olecranon fossa of humerus | `UBERON:0001679` | ethmoid bone | term name does not match parent label 'ethmoid bone' (likely misaligned) |
| olecranon of ulna | `UBERON:0012419` | taenia coli | parent UBERON:0012419 (taenia coli) is not a bone |
| olfactory foramina of ethmoid bone | `http://purl.org/sig/ont/fma/fma321806` | Hypothenar compartment of hand | parent ID is not a UBERON identifier |
| optic canal of sphenoid bone | `UBERON:0001627` | middle cerebral artery | parent UBERON:0001627 (middle cerebral artery) is not a bone |
| pecten pubis of pubis of os coxa | `UBERON:0001092` | vertebral bone 1 | term name does not match parent label 'vertebral bone 1' (likely misaligned) |
| pectinal line of femur | `UBERON:0001093` | vertebral bone 2 | term name does not match parent label 'vertebral bone 2' (likely misaligned) |
| pedicle of first cervical vertebra | `UBERON:0002378` | muscle of abdomen | parent UBERON:0002378 (muscle of abdomen) is not a bone |
| pedicle of second cervical vertebra | `https://purl.org/ccf/ASCTB-TEMP_periductal-branch-of-interlobular-artery-of-pancreas` | periductal branch of interlobular artery of pancreas | parent ID is not a UBERON identifier |
| perpendicular plate of ethmoid bone | `UBERON:8600078` | ascending pharyngeal artery | parent UBERON:8600078 (ascending pharyngeal artery) is not a bone |
| petrotympanic fissure of squamous part of temporal bone | `https://purl.org/ccf/ASCTB-TEMP_sole-of-foot-muscle` | sole of foot muscle | parent ID is not a UBERON identifier |
| posterior arch of first cervical vertebra | `UBERON:0001101` | external jugular vein | parent UBERON:0001101 (external jugular vein) is not a bone |
| posterior clinoid process of sphenoid bone | `http://purl.org/sig/ont/fma/fma276805` | Axillary lymph node | parent ID is not a UBERON identifier |
| posterior ethmoidal foramen of ethmoid bone | `UBERON:0001272` | innominate bone | term name does not match parent label 'innominate bone' (likely misaligned) |
| posterior gluteal line of ilium of os coxa | `UBERON:0001624` | anterior cerebral artery | parent UBERON:0001624 (anterior cerebral artery) is not a bone |
| posterior inferior iliac spine of ilium of os coxa | `https://purl.org/ccf/ASCTB-TEMP_superior-ulnar-lymph-node` | superior ulnar lymph node | parent ID is not a UBERON identifier |
| posterior sacral foramina of sacrum | `UBERON:0014685` | pterygoid plexus | parent UBERON:0014685 (pterygoid plexus) is not a bone |
| posterior superior iliac spine of ilium of os coxa | `http://purl.org/sig/ont/fma/fma52242` | Common cochlear artery | parent ID is not a UBERON identifier |
| posterior tubercle of first cervical vertebra | `https://purl.org/ccf/ASCTB-TEMP_posterior-radicular-vein` | posterior radicular vein | parent ID is not a UBERON identifier |
| postglenoid tubercle of squamous part of temporal bone | `https://purl.org/ccf/ASCTB-TEMP_antral-follicle` | antral follicle | parent ID is not a UBERON identifier |
| pterygoid canal of sphenoid bone | `UBERON:0001684` | mandible | term name does not match parent label 'mandible' (likely misaligned) |
| pterygoid fovea of mandible | `https://purl.org/ccf/ASCTB-TEMP_superior-pharyngeal-artery` | superior pharyngeal artery | parent ID is not a UBERON identifier |
| pterygoid hamulus of sphenoid bone | `http://purl.org/sig/ont/fma/fma46621` | Superior pharyngeal constrictor | parent ID is not a UBERON identifier |
| pubic symphysis of pubis of os coxa | `https://purl.org/ccf/ASCTB-TEMP_pelvic-floor-muscle` | pelvic floor muscle | parent ID is not a UBERON identifier |
| pubic tubercle of pubis of os coxa | `https://purl.org/ccf/ASCTB-TEMP_pelvic-floor-muscle` | pelvic floor muscle | parent ID is not a UBERON identifier |
| radial fossa of humerus | `https://purl.org/ccf/ASCTB-TEMP_lateral-lymphatic-pathway-of-upper-arm` | lateral lymphatic pathway of upper arm | parent ID is not a UBERON identifier |
| radial groove of humerus | `UBERON:0001423` | radius bone | term name does not match parent label 'radius bone' (likely misaligned) |
| radial tuberosity of radius | `http://purl.org/sig/ont/fma/fma71439` | Set of suboccipital muscles | parent ID is not a UBERON identifier |
| sacral tuberosity of sacrum | `UBERON:0004601` | rib 1 | term name does not match parent label 'rib 1' (likely misaligned) |
| scalene tubercle of first rib | `UBERON:0001427` | radiale | parent UBERON:0001427 (radiale) is not a bone |
| scaphoid tubercle of scaphoid | `UBERON:0006849` | scapula | term name does not match parent label 'scapula' (likely misaligned) |
| scapular spine of scapula | `http://purl.org/sig/ont/fma/fma43960` | Second plantar metatarsal artery | parent ID is not a UBERON identifier |
| sella turcica of sphenoid bone | `http://purl.org/sig/ont/fma/fma20966` | Prostatic part of inferior vesical artery | parent ID is not a UBERON identifier |
| shaft of first distal phalanx of hand | `UBERON:0004338` | proximal phalanx of manual digit 1 | term name does not match parent label 'proximal phalanx of manual digit 1' (likely misaligned) |
| shaft of first proximal phalanx of hand | `UBERON:0001423` | radius bone | term name does not match parent label 'radius bone' (likely misaligned) |
| shaft of radius of radius | `UBERON:0001424` | ulna | term name does not match parent label 'ulna' (likely misaligned) |
| shaft of ulna of ulna | `UBERON:0001250, https://purl.org/ccf/ASCTB-TEMP_non-penicillar-arteriole-of-spleen, UBERON:0005353` | red pulp of spleen, non-penicillar arteriole of spleen, spleen perifollicular zone | parent UBERON:0001250, https://purl.org/ccf/ASCTB-TEMP_non-penicillar-arteriole-of-spleen, UBERON:0005353 (red pulp of spleen, non-penicillar arteriole of spleen, spleen perifollicular zone) is not a bone |
| sternal region bone | `UBERON:0014477` | thoracic skeleton | term name does not match parent label 'thoracic skeleton' (likely misaligned) |

## Likely duplicates of existing UBERON terms (excluded from template)

| Proposed term | Likely existing UBERON ID | Match kind |
|---|---|---|
| acetabular fossa of os coxa | `UBERON:0014445` (`acetabular fossa`) | matches existing term name with bone qualifier stripped |
| acetabular notch of os coxa | `UBERON:0014446` (`acetabular notch`) | matches existing term name with bone qualifier stripped |
| acetabulum of os coxa | `UBERON:0001269` (`acetabulum`) | matches existing synonym with bone qualifier stripped |
| alae of sacrum | `UBERON:3010458` (`alae`) | matches existing synonym with bone qualifier stripped |
| anterior ethmoidal foramen of ethmoid bone | `UBERON:0018653` (`anterior ethmoidal foramen`) | matches existing term name with bone qualifier stripped |
| anterior inferior iliac spine of ilium of os coxa | `UBERON:0013709` (`anterior inferior iliac spine`) | matches existing term name with bone qualifier stripped |
| anterior superior iliac spine of ilium of os coxa | `UBERON:0013708` (`anterior superior iliac spine`) | matches existing term name with bone qualifier stripped |
| body of calcaneus | `UBERON:0000468` (`body`) | matches existing synonym with bone qualifier stripped |
| body of second cervical vertebra | `UBERON:0000468` (`body`) | matches existing synonym with bone qualifier stripped |
| body of sphenoid bone | `UBERON:0000468` (`body`) | matches existing synonym with bone qualifier stripped |
| calcaneal tuberosity of calcaneus | `UBERON:7500094` (`calcaneal tuberosity`) | matches existing synonym with bone qualifier stripped |
| carotid canal of petrous part of temporal bone | `UBERON:0006668` (`carotid canal`) | matches existing term name with bone qualifier stripped |
| foramen rotundum of sphenoid bone | `UBERON:0005446` (`foramen rotundum`) | matches existing term name with bone qualifier stripped |
| frontal sinus of frontal bone | `UBERON:0001760` (`frontal sinus`) | matches existing term name with bone qualifier stripped |
| groove for sigmoid sinus of mastoid part of temporal bone | `UBERON:0013420` (`groove for sigmoid sinus`) | matches existing term name with bone qualifier stripped |
| iliac fossa of ilium of os coxa | `UBERON:0011015` (`iliac fossa`) | matches existing term name with bone qualifier stripped |
| infraorbital foramen of maxilla | `UBERON:0018407` (`infraorbital foramen`) | matches existing synonym with bone qualifier stripped |
| infraorbital groove of maxilla | `UBERON:0018409` (`infraorbital groove`) | matches existing synonym with bone qualifier stripped |
| ischial ramus of ischium of os coxa | `UBERON:0014441` (`ischial ramus`) | matches existing term name with bone qualifier stripped |
| ischial spine of ischium of os coxa | `UBERON:0009000` (`ischial spine`) | matches existing term name with bone qualifier stripped |
| ischial tuberosity of ischium of os coxa | `UBERON:0034983` (`ischial tuberosity`) | matches existing term name with bone qualifier stripped |
| ischiopubic ramus of os coxa | `UBERON:0014440` (`ischiopubic ramus`) | matches existing term name with bone qualifier stripped |
| mandibular angle of mandible | `UBERON:0006959` (`mandibular angle`) | matches existing synonym with bone qualifier stripped |
| mandibular canal of mandible | `UBERON:0006673` (`mandibular canal`) | matches existing term name with bone qualifier stripped |
| mandibular condyle of mandible | `UBERON:0004657` (`mandibular condyle`) | matches existing synonym with bone qualifier stripped |
| mandibular neck of mandible | `UBERON:0004659` (`mandibular neck`) | matches existing synonym with bone qualifier stripped |
| mastoid process of mastoid part of temporal bone | `UBERON:0011220` (`mastoid process`) | matches existing synonym with bone qualifier stripped |
| maxillary sinus of maxilla | `UBERON:0001764` (`maxillary sinus`) | matches existing term name with bone qualifier stripped |
| mental foramen of mandible | `UBERON:0006812` (`mental foramen`) | matches existing term name with bone qualifier stripped |
| middle nasal concha of ethmoid bone | `UBERON:0005921` (`middle nasal concha`) | matches existing term name with bone qualifier stripped |
| neck of radius of radius | `UBERON:0000974` (`neck`) | matches existing term name with bone qualifier stripped |
| scapular neck of scapula | `UBERON:0018667` (`scapular neck`) | matches existing synonym with bone qualifier stripped |
| sphenoid sinus of sphenoid bone | `UBERON:0001724` (`sphenoid sinus`) | matches existing synonym with bone qualifier stripped |
| spinous process of first cervical vertebra | `UBERON:0001076` (`spinous process`) | matches existing synonym with bone qualifier stripped |
| spinous process of second cervical vertebra | `UBERON:0001076` (`spinous process`) | matches existing synonym with bone qualifier stripped |
| sternal body of sternum | `UBERON:0006820` (`sternal body`) | matches existing synonym with bone qualifier stripped |
| styloid process of petrous part of temporal bone | `UBERON:0003960` (`styloid process of petrous part of temporal bone`) | synonym |
| subscapular fossa of scapula | `UBERON:4200038` (`subscapular fossa`) | matches existing term name with bone qualifier stripped |
| superior nasal concha of ethmoid bone | `UBERON:0005920` (`superior nasal concha`) | matches existing term name with bone qualifier stripped |
| superior nuchal line of squamous part of occipital bone | `UBERON:0014803` (`superior nuchal line`) | matches existing synonym with bone qualifier stripped |
| superior orbital fissure of sphenoid bone | `UBERON:0005480` (`superior orbital fissure`) | matches existing term name with bone qualifier stripped |
| superior pubic ramus of pubis of os coxa | `UBERON:0014438` (`superior pubic ramus`) | matches existing term name with bone qualifier stripped |
| supraglenoid tubercle of scapula | `UBERON:0010760` (`supraglenoid tubercle`) | matches existing term name with bone qualifier stripped |
| temporal fossa of parietal bone | `UBERON:0013463` (`temporal fossa`) | matches existing term name with bone qualifier stripped |
| tibial tuberosity of tibia | `UBERON:7500062` (`tibial tuberosity`) | matches existing term name with bone qualifier stripped |
| transverse foramen of first cervical vertebra | `UBERON:0000130` (`transverse foramen`) | matches existing term name with bone qualifier stripped |
| transverse foramen of second cervical vertebra | `UBERON:0000130` (`transverse foramen`) | matches existing term name with bone qualifier stripped |
| transverse process of coccyx | `UBERON:0001077` (`transverse process`) | matches existing synonym with bone qualifier stripped |
| transverse process of first cervical vertebra | `UBERON:0001077` (`transverse process`) | matches existing synonym with bone qualifier stripped |
| transverse process of second cervical vertebra | `UBERON:0001077` (`transverse process`) | matches existing synonym with bone qualifier stripped |
| trochlear notch of ulna | `UBERON:0008449` (`trochlear notch`) | matches existing term name with bone qualifier stripped |
| ulnar tuberosity of ulna | `UBERON:4200184` (`ulnar tuberosity`) | matches existing term name with bone qualifier stripped |
| vertebral arch of eighth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of eleventh thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of fifth cervical vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of fifth lumbar vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of fifth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of first lumbar vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of first thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of fourth cervical vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of fourth lumbar vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of fourth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of ninth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of second cervical vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of second lumbar vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of second thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of seventh cervical vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of seventh thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of sixth cervical vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of sixth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of tenth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of third cervical vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of third lumbar vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of third thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral arch of twelfth thoracic vertebra | `UBERON:0010358` (`vertebral arch`) | matches existing synonym with bone qualifier stripped |
| vertebral body of eighth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of eleventh thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of fifth cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of fifth lumbar vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of fifth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of first cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of first lumbar vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of first thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of fourth cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of fourth lumbar vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of fourth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of ninth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of second cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of second lumbar vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of second thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of seventh cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of seventh thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of sixth cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of sixth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of tenth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of third cervical vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of third lumbar vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of third thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral body of twelfth thoracic vertebra | `UBERON:0001075` (`vertebral body`) | matches existing synonym with bone qualifier stripped |
| vertebral foramen of first cervical vertebra | `UBERON:0001131` (`vertebral foramen`) | matches existing term name with bone qualifier stripped |
| vertebral foramen of first thoracic vertebra | `UBERON:0001131` (`vertebral foramen`) | matches existing term name with bone qualifier stripped |
| vertebral foramen of second cervical vertebra | `UBERON:0001131` (`vertebral foramen`) | matches existing term name with bone qualifier stripped |
