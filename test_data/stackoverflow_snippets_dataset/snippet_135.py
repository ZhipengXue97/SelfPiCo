# Extracted from https://stackoverflow.com/questions/9001509/how-do-i-sort-a-dictionary-by-key
dict1 = {'renault': 3, 'ford':4, 'volvo': 1, 'toyota': 2} 
dict2 = {}                  # create an empty dict to store the sorted values
for key in sorted(dict1.keys()):
    if not key in dict2:    # Depending on the goal, this line may not be neccessary
        dict2[key] = dict1[key]

dict1 = {'renault': 3, 'ford':4, 'volvo': 1, 'toyota': 2} 
dict2 = {}                  # create an empty dict to store the sorted     values
for key in sorted(dict1.keys()):
    if not key in dict2:    # Depending on the goal, this line may not be  neccessary
        value = dict1[key]
        dict2[key] = value

