import re
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('all')

# Sample text
text = "NLP is amazing! It helps computers understand human language. Can't wait to learn more."

# Lowercasing
text = text.lower()

# Removing punctuation
text = re.sub(r'[^\w\s]', '', text)

# Tokenization
tokens = word_tokenize(text)

# Removing stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

print(tokens)  # Output: ['nlp', 'amazing', 'help', 'computer', 'understand', 'human', 'language', 'wait', 'learn']
