# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def func1(a, b):
    c = (a + b)
    def inside_func1(c):
        print("c="+ str(a + b))
    return inside_func1(c)

func1(2, 3)

# def fun1():
#     print("Func1")
#
# def func2():
#     return fun1()
#
# func2()


