# News headlines experiments

NER model trained on a small number of annotations and base model `en_core_web_lg`
with original NER pipeline removed.

## Training

```bash
$ prodigy train ner ner_news_headlines models/en_core_web_lg_no_ner --output models/model_news_headlines
✔ Loaded model 'models/en_core_web_lg_no_ner'
Created and merged data for 172 total examples
Using 86 train / 86 eval (split 50%)
Component: ner | Batch size: compounding | Dropout: 0.2 | Iterations: 10
ℹ Baseline accuracy: 0.000

=========================== ✨  Training the model ===========================

#    Loss       Precision   Recall     F-Score
--   --------   ---------   --------   --------
 1     133.08      22.222     14.286     17.391
 2      69.33      51.613     38.095     43.836
 3      29.88      85.714     57.143     68.571
 4      31.79      81.250     61.905     70.270
 5      19.47      77.778     66.667     71.795
 6       6.65      78.049     76.190     77.108
 7      10.84      86.111     73.810     79.487
 8       5.81      88.235     71.429     78.947
 9       2.52      90.625     69.048     78.378
10       2.07      85.714     71.429     77.922

============================= ✨  Results summary =============================

Label    Precision   Recall   F-Score
------   ---------   ------   -------
PERSON      84.615   78.571    81.481
ORG         86.957   71.429    78.431


Best F-Score   79.487
Baseline       0.000
```

## Tests

> Ben Bernanke, the former Federal Reserve chairman credited with rescuing the American economy
> from the 2008 crisis, issued a similar warning Wednesday. Jane Halliday, who studied the Great Depression,
> said the current situation is 'more like a major snowstorm or natural disaster than a Great Depression-style
>downturn.' She quoted the interview Tony Atwood gave for NBC earlier.

```python
[('Ben Bernanke', 'PERSON'),
 ('Jane Halliday', 'PERSON'),
 ('Tony Atwood', 'PERSON'),
 ('NBC', 'PERSON')]
```
