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
    token = tu.simple_tokenize(doc)
    doc_vector = [0 for _ in word_to_id]
    for word in token:
        if word in word_to_id:
            doc_vector[word_to_id[word]] = 1

    doc_vectors.append(doc_vector)

df = pd.DataFrame(doc_vectors, columns=id_to_word.values())
print(df)