import txtutils as tu
import pandas as pd

docs = []
docs.append("I am going to go to the store.")
docs.append("The Science of today is the technology of tommorow.")
docs.append("You are using pip version 3.")
docs.append("Could not install packages due to an Error.")

word_to_id, id_to_word = tu.buildDict(docs)
doc_vectors = []
for doc in docs:
    doc_vector = []
    token = tu.simple_tokenize(doc)
    for word in token:
        vector = [0 for _ in word_to_id]
        vector[word_to_id[word]] = 1
        doc_vector.append(vector)
    doc_vectors.append(doc_vector)

for doc, doc_vector in zip(docs, doc_vectors):
    df = pd.DataFrame(doc_vector, columns=id_to_word.values())
    print(doc)
    print(df)

