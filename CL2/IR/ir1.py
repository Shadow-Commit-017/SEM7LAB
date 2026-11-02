
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Step 1: Input text document
text = """
Natural Language Processing is an important field
of Artificial Intelligence. It helps computers
understand and process human languages.
"""

print("Original Text:")
print(text)

# Step 2: Convert text into lowercase
text = text.lower()

# Step 3: Remove punctuation and special characters
text = re.sub(r'[^a-z\s]', '', text)

# Step 4: Tokenization
words = word_tokenize(text)

print("\nTokenized Words:")
print(words)

# Step 5: Remove stop words
stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word not in stop_words
]

print("\nAfter Stop Word Removal:")
print(filtered_words)

# Step 6: Perform stemming
stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word)
    for word in filtered_words
]

print("\nAfter Stemming:")
print(stemmed_words)

# Step 7: Final pre-processed document
final_text = " ".join(stemmed_words)

print("\nFinal Pre-processed Text:")
print(final_text)
