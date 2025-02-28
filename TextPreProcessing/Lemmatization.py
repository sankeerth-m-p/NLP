import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("running", pos="v"))  # Output: run
print(lemmatizer.lemmatize("better", pos="a"))  # Output: good
