import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
tokens = word_tokenize("I'm learning NLP with NLTK!")
print(tokens)  # ['I', "'m", 'learning', 'NLP', 'with', 'NLTK', '!']
