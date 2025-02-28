import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("I'm learning NLP with spaCy!")
tokens = [token.text for token in doc]
print(tokens)  # ['I', "'m", 'learning', 'NLP', 'with', 'spaCy', '!']
