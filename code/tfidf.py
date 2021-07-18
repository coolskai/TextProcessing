from collections import Counter
import copy
import numpy as np
import math
import preprocess as proc

def make_doc_vectors(corpus, word_to_id):
    doc_vectors = {}
    zero_vector = [0 for _ in range((len(word_to_id)))]
    for doc_id, doc in corpus.items():
        vec = copy.copy(zero_vector)
        word_count = Counter(doc)
        for key, value in word_count.items():
            vec[key] = value
        doc_vectors[doc_id] = vec
    return doc_vectors
def logscale_tf_vector(tf_vectors):
    doc_vectors = {}
    zero_vector = [0.0 for _ in range((len(word_to_id)))]
    for doc_id, doc in corpus.items():
        vec = copy.copy(zero_vector)
        word_count = Counter(doc)
        for key, value in word_count.items():
            vec[key] = 1+ math.log2(value)
        doc_vectors[doc_id] = vec
    return doc_vectors
def idf_dict(id_to_word, tf_vectors):
    idf_dict = {}
    N = len(tf_vectors)
    for id, _ in id_to_word.items():
        idf_dict[id] = 0.0
        for _, doc in tf_vectors.items():
            if doc[id] > 0:
                idf_dict[id] += 1
    idf_dict = {id : math.log2(N/val) for id, val in idf_dict.items()}
    return idf_dict  
def idf_list(tn, tf_vectors):
    idf_vector = [0.0 for _ in range(tn)]
    N = len(tf_vectors)
    print(N)
    for _, value in tf_vectors.items():
        i = 0
        for val in value:
            if val > 0:
                idf_vector[i] += 1
            i += 1
    idf_vector = [math.log2(N/val) for val in idf_vector]
    return idf_vector
def tfidf(tf_vectors, idf_dict):
    tfidf_vectors = {}
    idf = [val for _, val in idf_dict.items()]
    zero_vector = [0.0 for _ in range(len(idf_dict))]
    for doc_id, doc in tf_vectors.items():
        vec = copy.copy(zero_vector)
        vec = np.multiply(doc, idf)
        tfidf_vectors[doc_id] = vec
    return tfidf_vectors   

if __name__ == '__main__':
    docs = []
    docs.append('To do is to be. To be is to do.')
    docs.append('To be or not to be. I am what I am')
    docs.append('I think therefore I am. Do be do be do.')
    docs.append('Do do do da da da. Let it be let it be.')

    id_to_doc, word_to_id, id_to_word = proc.build_dict(docs)
    corpus = proc.build_corpus(id_to_doc, word_to_id)
    tf_vectors = make_doc_vectors(corpus, word_to_id)
    tf_vectors = logscale_tf_vector(tf_vectors)
    idf_lst = idf_list(len(word_to_id), tf_vectors)
    print(idf_lst)
    idf_dic = idf_dict(id_to_word, tf_vectors)
    for id, idf in idf_dic.items():
        print('#id : %2d %10s #idf : %6.4f'%(id, id_to_word[id], idf))
    tfidf = tfidf(tf_vectors, idf_dic)
    for doc_id, result in tfidf.items():
        print('#doc-id : %2d '%(doc_id))
        for word_id, _ in id_to_word.items():
            print('#id : %2d #tfidf : %6.4f'%(word_id, result[word_id]))
        