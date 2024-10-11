# Extracted from https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl
class X():
    def __init__(self):
        print("X")

class Y(X):
    def __init__(self):
        # X.__init__(self)
        super(Y, self).__init__()
        print("Y")

class P(X):
    def __init__(self):
        super(P, self).__init__()
        print("P")

class Q(Y, P):
    def __init__(self):
        super(Q, self).__init__()
        print("Q")

Q()

X
Y
Q

X
P
Y
Q

