import txtutils as tu
import pandas as pd
import numpy as np

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

############ 실습코드 구현 ############
print("<<<<df.T를 활용하여 출력한 결과>>>>")
print(df.T)

table = df.to_numpy()
table = table.T
keyword = input("input keyword : ")
if keyword in word_to_id:
    for i, val in enumerate(table[word_to_id[keyword]]):
        if val == 1:
            print('doc_num = {}. Text : {}'.format(i, docs[i]))

else:
    print('키워드 없음')