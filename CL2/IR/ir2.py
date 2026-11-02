
import re
from collections import defaultdict

# Step 1: Create sample documents
documents = {
    "D1": "Python is a programming language",
    "D2": "Python is used in data science",
    "D3": "Data science uses machine learning",
    "D4": "Programming is important for computer science"
}

# Step 2: Create inverted index
inverted_index = defaultdict(list)

for doc_id, text in documents.items():

    # Convert text into lowercase
    text = text.lower()

    # Remove special characters
    words = re.findall(r'\b\w+\b', text)

    # Add words to inverted index
    for word in set(words):
        inverted_index[word].append(doc_id)

# Step 3: Display inverted index
print("INVERTED INDEX")

for word, doc_ids in sorted(inverted_index.items()):
    print(word, ":", doc_ids)

# Step 4: Search for a document
query = input("\nEnter search word: ").lower()

# Step 5: Retrieve matching documents
if query in inverted_index:

    print("\nDocuments containing", query, ":")

    for doc_id in inverted_index[query]:
        print(doc_id, ":", documents[doc_id])

else:
    print("\nNo matching documents found.")
