# COVID-19 Open Research Dataset Challenge (CORD-19)

Kaggle challenge: [CORD-19]](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Task: [What do we know about COVID-19 risk factors?](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/tasks?taskId=558)

## Prodigy

```bash
# start Prodigy and annotate some entities with patterns
# https://prodi.gy/docs/named-entity-recognition#manual-patterns
prodigy ner.manual ner_news_headlines en_core_web_lg data/raw/news_headlines.jsonl \
  --label PERSON,ORG --patterns patterns/PERSON_ORG.jsonl

# save annotations to a file
prodigy db-out ner_news_headlines > data/annotated/ner_news_headlines.jsonl

# data-to-spacy
TODO - understand this recipe

# train model
prodigy train ner ner_news_headlines en_core_web_lg --output models/

# predict
TODO
```

### Misc

[When to reject when annotating text for NER?](https://support.prodi.gy/t/when-to-reject-in-ner-manual-or-ner-make-gold/892/2)
(never - accept both highlights and samples with no spans)

[`batch-train` is deprecated](https://prodi.gy/docs/recipes#deprecated)
