class A:
    def __init__(self, param):
        self.first = param

class B(A):
    pass

b = B(1)
print(b.first)