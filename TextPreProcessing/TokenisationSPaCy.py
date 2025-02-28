import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp(input(">>"))
tokens = [token.text for token in doc]
print(tokens)
