# define three dictionaries 
dict1 = {1: 10, 2:20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# create an empty dictionary
new_dict = {} 
# update empty dictionary with above three dictionarys
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

# new dictionary contains the key values pairs from
# dict1, dict2, and dict3
print(new_dict)
