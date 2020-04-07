# COVID-19 Open Research Dataset Challenge (CORD-19)

Kaggle challenge: [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Task: [What do we know about COVID-19 risk
factors?](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/tasks?taskId=558)

## Dataset citation

COVID-19 Open Research Dataset (CORD-19). 2020. Version 2020-03-13.
Retrieved from https://pages.semanticscholar.org/coronavirus-research.
Accessed 2020-03-26. doi:10.5281/zenodo.3715506

## Prodigy

### Annotations

```bash
# manual annotation with suggestions from patterns
# https://prodi.gy/docs/named-entity-recognition#manual-patterns
prodigy ner.manual cord_19_abstracts en_core_web_lg data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RISK_FACTOR.jsonl

# accept or reject suggestions from patterns
# https://prodi.gy/docs/recipes#match
prodigy match cord_19_abstracts_match models/en_core_web_lg_no_ner data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RF_list_2020.03.17.20037572.jsonl --label-span

# manual annotation with suggestions from patterns and existing model in the loop
# https://prodi.gy/docs/recipes#ner-teach
prodigy ner.teach cord_19_abstracts_teach models/2020_03_28_match/en_rf_web_lg data/raw/cord_19_abstracts_filtered.jsonl \
  --label RISK_FACTOR --patterns patterns/RF_list_2020.03.17.20037572.jsonl
```

### Training

```bash
# train model
prodigy train ner cord_19_abstracts_match models/en_core_web_lg_no_ner --output models/2020_03_28_match/en_rf_web_lg
```

### Other

```bash
# save annotations to a file
prodigy db-out cord_19_abstracts > data/annotated/cord_19_abstracts.jsonl
```

### Misc

1. [When to reject when annotating text for NER?](https://support.prodi.gy/t/when-to-reject-in-ner-manual-or-ner-make-gold/892/2)
1. [When should I press accept, reject or ignore?](https://prodi.gy/docs/named-entity-recognition#manual-accept-reject)
(never - accept both highlights and samples with no spans)
1. [`batch-train` is deprecated](https://prodi.gy/docs/recipes#deprecated)

## Raw data filtering

```bash
fgrep "risk factor" data/raw/cord_19_abstracts.jsonl > data/raw/cord_19_abstracts_filtered.jsonl
```

## GPU support in spaCy

For GPU support, you must install spaCy with a following command:

```bash
pip install -U spacy[cuda]

pip install -U spacy[cuda92]  # if you know your CUDA version
```

More information:

- [Run spaCy with GPU](https://spacy.io/usage#gpu)
- [What do square brackets mean in pip install?](https://stackoverflow.com/q/46775346/95)

### GPU and WSL

I was unable to install `spacy[cuda]` using WSL. Lack of GPU support? Lack of appropriate drivers?
