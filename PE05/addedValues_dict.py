# define two dictionarys with some shared keys
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

# for each key in the first dictionary
for letter in dict1.keys():
    # if key is in the second dictionary
    if letter in dict2:
        # update key, value pair with the added values of the shared key
        dict2[letter] = dict1[letter] + dict2[letter]
    # if key is not shared continue for loop
    else:
        continue

# update dict1 with updated dict2
dict1.update(dict2)

# dict1 now has the updated key, values pairs with the added values
print(dict1)
