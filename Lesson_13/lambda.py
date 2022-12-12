# >>> (lambda x, y, z: x + y + z)(1, 2, 3)
# 6
# >>> (lambda x, y, z=3: x + y + z)(1, 2)
# 6
# >>> (lambda x, y, z=3: x + y + z)(1, y=2)
# 6
# >>> (lambda *args: sum(args))(1,2,3)
# 6
# >>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
# 6
# >>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
# 6


# # task 1
# def square (x):
#     return x**2

# def cube(x):
#     return x**3

# func_dict = {'square': square,
#              'cube': cube}
# for key in func_dict:
#     print(func_dict[key](5))

# # task 2
# a = lambda x,y: x**y
# print(a(2,8))

# # task 3
# def count_a(arr:list):
#     return [i.lower().count('a') for i in arr]

# list_1 = ['name', 'drive', 'Anna', 'who', 'Java', 'additional','hi']
# print(count_a(list_1))

# # lambda
# my_list = list(map(lambda x: x.lower().count('a'), list_1))
# print(my_list)

# # task 4
# def mul(n):
#     def second_step(y):
#         step = n*y
#         return lambda x: x*step
#     return second_step

# a = mul(5)
# print(a.__name__)
# print(a)
# b = a(9)
# print(b.__name__)
# c = b(2)
# print(type(c))
# print(c)
# a = mul(5)(9)(2)
# print(a)

# # task 5
# def make_quadratic(a:int, b:int, c:int):
#     def solve(x:int):
#         return True if a*x**2 + b*x + c == 0 else False
#     return solve

# f1 = make_quadratic(1,-5,0)
# print(f1(5))

import json
# task 6
dict_1 = {'name': 'Yaroslav',
         'surname': 'Artiushenko',
         'age': 21}
dict_2 = {'name': 'Andrey',
          'surname': 'Ivanenko',
          'age': 25}
dict_3 = {'name': 'Banton',
          'surname': 'Nikitin',
          'age': 23}

name_list = [dict_1, dict_2, dict_3]

def sort_type(arr:list, key: str):
    return sorted(arr, key = lambda x: x[key])

print(sort_type(name_list, 'age'))
print(sort_type(name_list, 'name'))

with open('sort1.json', 'w') as file:
    file.write(json.dumps(sort_type(name_list, 'age')))

with open('sort2.json', 'w') as file:
    file.write(json.dumps(sort_type(name_list, 'name')))