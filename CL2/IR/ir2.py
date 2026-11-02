# Step 1: Create documents
documents = {
    "D1": "Machine Learning is useful",
    "D2": "Machine Learning uses data",
    "D3": "Data Science is useful"
}

# Step 2: Create inverted index
inverted_index = {}

for doc_id, text in documents.items():
    for word in text.lower().split():
        inverted_index.setdefault(word, []).append(doc_id)

# Step 3: Display inverted index
print("Inverted Index:")
print(inverted_index)

# Step 4: Search a word
query = input("\nEnter search word: ").lower()

# Step 5: Display matching documents
print("Matching Documents:",
      inverted_index.get(query, "No documents found"))
