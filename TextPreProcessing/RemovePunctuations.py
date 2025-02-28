import re
text = "Hello! How's your diet going? #Fitness #Healthy"
text_clean = re.sub(r'[^\w\s]', '', text)
print(text_clean)  # Output: Hello Hows your diet going Fitness Healthy
