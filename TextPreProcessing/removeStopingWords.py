import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Example text
text = input(">>")

# Tokenize text
tokens = word_tokenize(text)

# Load stopwords
stop_words = set(stopwords.words('english'))

# Filter out stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Print the cleaned tokens
print(filtered_tokens)
