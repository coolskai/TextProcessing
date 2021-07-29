import txtutils as tutil
docs = []
docs.append("I am going to go to the store.")
docs.append("The Science of today is the technology of tommorow.")
docs.append("You are using pip version 3.")
docs.append("Could not install packages due to an Error.")

word_to_id, id_to_word = tutil.buildDict(docs)
print(word_to_id)
print(id_to_word)
