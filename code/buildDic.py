docs = []
docs.append("I am going to go to the store.")
docs.append("The Science of today is the technology of tommorow.")
docs.append("You are using pip version 3.")
docs.append("Could not install packages due to an Error.")

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

print(word_to_id)
print(id_to_word)
keys = id_to_word.keys()
values = id_to_word.values()
for key, val in zip(keys, values):
    print(key, val)
