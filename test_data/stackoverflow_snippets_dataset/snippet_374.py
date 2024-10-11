# Extracted from https://stackoverflow.com/questions/5900578/collections-defaultdict-difference-with-normal-dict
somedict = {}
print(somedict[3]) # KeyError

someddict = defaultdict(int)
print(someddict[3]) # print int(), thus 0

