def simple_tokenizer(doc):
    doc = doc.lower()
    doc = doc.replace('.', ' .')
    tokens = doc.split(' ')
    return tokens
def build_dict(docs):    
    word_to_id = {}
    id_to_word = {}
    id_to_doc = {}
    id = 0
    for doc in docs:
        words = simple_tokenizer(doc)
        id_to_doc[id] = words
        for word in words:
            if word not in word_to_id:
                new_id = len(word_to_id)
                word_to_id[word] = new_id
                id_to_word[new_id] = word
        id += 1
    return id_to_doc, word_to_id, id_to_word
def build_corpus(id_to_doc, word_to_id):
    corpus = {}
    for key, value in id_to_doc.items():
        corpus[key] = [word_to_id[w] for w in value]
    return corpus
    
if __name__ == '__main__':
    docs = []
    docs.append('To do is to be. To be is to do.')
    docs.append('To be or not to be. I am what I am')
    docs.append('I think therefore I am. Do be do be do.')
    docs.append('Do do do da da da. Let it be let it be.')

    id_to_doc, word_to_id, id_to_word = build_dict(docs)
    corpus = build_corpus(id_to_doc, word_to_id)
    print(corpus)
