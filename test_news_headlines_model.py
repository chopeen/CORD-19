import spacy
from pprint import pprint

text = """Ben Bernanke, the former Federal Reserve chairman credited with rescuing the American economy
from the 2008 crisis, issued a similar warning Wednesday. Jane Halliday, who studied the Great Depression,
said the current situation is 'more like a major snowstorm or natural disaster than a Great Depression-style
downturn.' She quoted the interview Tony Atwood gave for NBC earlier."""

nlp = spacy.load("models/model_news_headlines")
doc = nlp(text)

pprint([(ent.text, ent.label_) for ent in doc.ents])
