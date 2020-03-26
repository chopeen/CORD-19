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
# start Prodigy and annotate some entities with patterns
# https://prodi.gy/docs/named-entity-recognition#manual-patterns
prodigy ner.manual cord_19_abstracts en_core_web_lg data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RISK_FACTOR.jsonl

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

[When to reject when annotating text for NER?](https://support.prodi.gy/t/when-to-reject-in-ner-manual-or-ner-make-gold/892/2)
(never - accept both highlights and samples with no spans)

[`batch-train` is deprecated](https://prodi.gy/docs/recipes#deprecated)
