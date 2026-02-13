# 🧠 Your Task: Tokenize the story from 'story.txt' using NLTK's sent_tokenize and word_tokenize functions

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re

# Make sure required NLTK resources are available
nltk.download('punkt')
nltk.download('punkt_tab')

# 1. Open and read the story text
with open('story.txt', 'r') as file:
    story = file.read()

# 2. (Optional) Remove any unwanted characters using re.sub
# For example: remove extra whitespace or punctuation symbols
# Removes HTML tags like <div>
clean_story = re.sub(r'<[^>]+>', '', story) 
# Then normalize whitespace
clean_story = re.sub(r'\s+', ' ', clean_story).strip()

# 3. Tokenize the story into sentences
sentences = sent_tokenize(clean_story)

# 4. Tokenize the story into words
words = word_tokenize(clean_story)

# 5. Print results
print("=== Sentences ===")
for sentence in sentences:
    print(sentence)

print("\n=== Words ===")
for word in words:
    print(word)
