# COVID-19 Open Research Dataset Challenge (CORD-19)

Kaggle challenge: [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Task: [What do we know about COVID-19 risk
factors?](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/tasks?taskId=558)

## Dataset citation

COVID-19 Open Research Dataset (CORD-19). 2020. Version 2020-03-13.
Retrieved from https://pages.semanticscholar.org/coronavirus-research.
Accessed 2020-03-26. doi:10.5281/zenodo.3715506

## Prodigy

```bash
# manual annotation with suggestions from patterns
# https://prodi.gy/docs/named-entity-recognition#manual-patterns
prodigy ner.manual cord_19_abstracts en_core_web_lg data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RISK_FACTOR.jsonl

# accept or reject suggestions from patterns
# https://prodi.gy/docs/recipes#match
prodigy match cord_19_abstracts_match models/en_core_web_lg_no_ner data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RF_list_2020.03.17.20037572.jsonl --label-span

# save annotations to a file
prodigy db-out cord_19_abstracts > data/annotated/cord_19_abstracts.jsonl

# train model
prodigy train ner cord_19_abstracts models/en_core_web_lg_no_ner --output models/modelX
```

## Raw data filtering

```bash
fgrep "risk factor" data/raw/cord_19_abstracts.jsonl > data/raw/cord_19_abstracts_filtered.jsonl
```

### Misc

1. [When to reject when annotating text for NER?](https://support.prodi.gy/t/when-to-reject-in-ner-manual-or-ner-make-gold/892/2)
1. [When should I press accept, reject or ignore?](https://prodi.gy/docs/named-entity-recognition#manual-accept-reject)
(never - accept both highlights and samples with no spans)
1. [`batch-train` is deprecated](https://prodi.gy/docs/recipes#deprecated)
