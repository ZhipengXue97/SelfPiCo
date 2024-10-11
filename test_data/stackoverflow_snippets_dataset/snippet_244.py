# Extracted from https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
ages = {"Harry": 17, "Lucy": 16, "Charlie": 18}
print(sorted(ages, key=ages.get))
['Lucy', 'Harry', 'Charlie']
print(max(ages, key=ages.get))
Charlie
print(min(ages, key=ages.get))
Lucy

