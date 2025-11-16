#this is a simple example of tokenization and vocabulary creation in Pytho
data_set = ["I love movies", "I hate bad movies"]
# Tokenization and vocabulary creation
token_list = list(map(str.split, data_set))
print(token_list)

size_data = len(data_set)
vocabulary = data_set[0].split() + data_set[1].split()
vocabulary = list(dict.fromkeys(vocabulary))
print(vocabulary)

nlist = []
x = 0
full_list = []
#loop thrugh however many sentenances there are in the data set
for i in range(size_data):
    for word in vocabulary:
        x = token_list[i].count(word)
        nlist.append(x)
    full_list.append(nlist.copy())
    nlist.clear()

print(full_list)



