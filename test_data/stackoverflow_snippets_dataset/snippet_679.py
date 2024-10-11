# Extracted from https://stackoverflow.com/questions/2158395/flatten-an-irregular-arbitrarily-nested-list-of-lists
a = [1, 2, 3, 5, 10, [1, 25, 11, [1, 0]]]    
g = str(a).replace('[', '').replace(']', '')    
b = [int(x) for x in g.split(',') if x.strip()]

