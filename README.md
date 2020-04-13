# COVID-19 Open Research Dataset Challenge (CORD-19)

Kaggle challenge: [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Task: [What do we know about COVID-19 risk
factors?](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/tasks?taskId=558)

## Dataset citation

COVID-19 Open Research Dataset (CORD-19). 2020. Version 2020-03-13.  
Retrieved from https://pages.semanticscholar.org/coronavirus-research.  
Accessed 2020-03-26. doi:10.5281/zenodo.3715506

## Experiments

For early experiments, see [train_experiments_1.ipynb](./backup_early_experiments/train_experiments_1.ipynb). They used
full article abstracts for annotation and training.

Further work is documented in [train_experiments_2.ipynb](./train_experiments_2.ipynb) and the previous datasets
were replaced with a small file `cord_19_rf_sentences.jsonl` prepared by Adrianna Safaryn and Cezary Szulc
(see the [Kaggle notebook](https://www.kaggle.com/cezaryszulc/kaggle-covid-19-competition) for details):

```txt
+------------------+           +------------------+           +------------------+
|                  |           |                  |           |                  |          +----------------------------+
|                  |  FILTER   | Abstracts and    |  FILTER   | Sentences that   |          |                            |
| CORD-19 dataset  +---------->| articles that    +---------->| contain phrase   +--------> | cord_19_rf_sentences.jsonl |
|                  |           | mention COVID-19 |           | "risk factor(s)  |          |                            |
|                  |           | and synonyms     |           |                  |          +----------------------------+
+------------------+           +------------------+           +------------------+
```

## Prodigy notes

1. [When to reject when annotating text for NER?](https://support.prodi.gy/t/when-to-reject-in-ner-manual-or-ner-make-gold/892/2)
1. [When should I press accept, reject or ignore?](https://prodi.gy/docs/named-entity-recognition#manual-accept-reject)
(never - accept both highlights and samples with no spans)
1. [`batch-train` is deprecated](https://prodi.gy/docs/recipes#deprecated)

## Raw data filtering

```bash
fgrep "risk factor" data/raw/cord_19_abstracts.jsonl > data/raw/cord_19_abstracts_filtered.jsonl
```
