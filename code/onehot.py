import pandas as pd

sent = 'Thomas Jefferson began building Monticello at the age of 26.'
token = sent.split()
vocab = sorted(set(token))
print(vocab)

one_hot_vectors = []

for idx, word in enumerate(token):
    vector = [0 for _ in vocab]
    vector[vocab.index(word)] = 1
    one_hot_vectors.append(vector)

for idx, vec in enumerate(one_hot_vectors):
    print('token = {} : vector : {}'.format(token[idx], vec))

df = pd.DataFrame(one_hot_vectors, columns=vocab)
print(df)


