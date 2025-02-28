import spacy

# Load a small model
nlp = spacy.load("en_core_web_sm")

# Example sentence
sentence = "I want to lose 5 kilograms in a month by running 10 miles per week."

# Process the sentence
doc = nlp(sentence)

# Extract named entities
for ent in doc.ents:
    print(ent.text, ent.label_)
