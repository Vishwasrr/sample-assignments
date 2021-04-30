class A:

    a = 10
    b = 20

    @classmethod
    def change(cls, a, b):
        cls.a = a
        cls.b = b

obj = A()
print(A.a, A.b)
obj.change(100, 200)
print(A.a, A.b)


    
