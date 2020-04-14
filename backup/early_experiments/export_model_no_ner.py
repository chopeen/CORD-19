import spacy

base_model = "en_core_web_lg"

nlp = spacy.load(base_model)
nlp.disable_pipes("ner")
nlp.to_disk(f"models/{base_model}_no_ner")
