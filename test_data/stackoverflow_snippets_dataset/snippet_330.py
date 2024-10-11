# Extracted from https://stackoverflow.com/questions/10712002/create-an-empty-list-with-certain-size-in-python
xs = list();
for i in range(0, 9):
   xs.append(i)

xs = []
for i in range(10):
    xs.append(i)

xs = range(10) # 2.x specific!
# In 3.x, we don't get a list; we can do a lot of things with the
# result, but we can't e.g. append or replace elements.

xs = list(range(10)) # correct in 3.x, redundant in 2.x

