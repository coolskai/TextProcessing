#txtutils.py
def simple_tokenize(txt):
    '''
    간단한 토크나이징 함수
    :param txt: 문자열
    :return: 토큰 리스트
    '''
    txt = txt.lower()
    txt = txt.replace('.', ' .')
    token = txt.split()
    return token

def buildDict(docs):
    '''
    :param docs: 문자열을 요소로 가진 리스트
    :return: 단어>>id, id>>단어 사전
    '''
    word_to_id = {}
    id_to_word = {}
    for doc in docs:
        doc = doc.lower()
        doc = doc.replace('.', ' .')
        token = doc.split()
        for word in token:
            if word not in word_to_id:
                new_id = len(word_to_id)
                word_to_id[word] = new_id
                id_to_word[new_id] = word
    return word_to_id, id_to_word

if __name__ == '__main__':
    docs = []
    docs.append("I am going to go to the store.")
    docs.append("The Science of today is the technology of tommorow.")
    docs.append("You are using pip version 3.")
    docs.append("Could not install packages due to an Error.")

    word_to_id, id_to_word = buildDict(docs)
    print(word_to_id)
    print(id_to_word)
