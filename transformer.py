from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

# Example text
text = "Transformers have revolutionized NLP!"

# Tokenize input
inputs = tokenizer(text, return_tensors="pt")

# Get model output
outputs = model(**inputs)

# Print logits
print(outputs.logits)
