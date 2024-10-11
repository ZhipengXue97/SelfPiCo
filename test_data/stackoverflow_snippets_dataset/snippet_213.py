# Extracted from https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
someTuple = (1,2)
someList  = [1,2] 

a = tuple(range(1000))
b = list(range(1000))

a.__sizeof__() # 8024
b.__sizeof__() # 9088

b    = [1,2]   
b[0] = 3       # [3, 2]

a    = (1,2)
a[0] = 3       # Error

a     = (1,2)
b     = [1,2]  

id(a)          # 140230916716520
id(b)          # 748527696

a   += (3,)    # (1, 2, 3)
b   += [3]     # [1, 2, 3]

id(a)          # 140230916878160
id(b)          # 748527696

a    = (1,2)
b    = [1,2] 

c = {a: 1}     # OK
c = {b: 1}     # Error

