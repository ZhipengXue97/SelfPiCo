# Extracted from https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration
x=[1,2,3,4]

y=iter(x)

y=[1,2,3,4]

y.next()
1
y.next()
2
y.next()
3
y.next()
4
y.next()
StopIteration

