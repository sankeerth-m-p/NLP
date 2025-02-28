import re
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    # Lowercasing
    text = text.lower()
    
    # Removing punctuation
    text = re.sub(r"[^\w\s]", "", text)
    
    # Tokenization
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.text not in stop_words]
    
    return " ".join(tokens)

text = "I need a high-protein diet to gain muscle mass!"
print(preprocess_text(text))  # Output: need high protein diet gain muscle mass
