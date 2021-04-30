class A:
    a = 10
    b = 20

    @staticmethod
    def calci(a, b):
        a = a + 5
        b = b + 5
        print(a, b)
        

obj = A()
print(A.a, A.b)
obj.calci(10, 20)
print(A.a, A.b)

