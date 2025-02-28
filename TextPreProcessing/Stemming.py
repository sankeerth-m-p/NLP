import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("running"))  # Output: run
print(stemmer.stem("better"))   # Output: better (incorrect!)
