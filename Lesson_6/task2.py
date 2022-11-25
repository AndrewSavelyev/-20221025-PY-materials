# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers
import random
i = 1
list_1 = [random.randint(1, 10)]
list_2 = [random.randint(1, 10)]
while i < 10:
    list_1 = list_1 + [random.randint(1, 10)]
    list_2 = list_2 + [random.randint(1, 10)]
    i += 1
print(list_1)
print(list_2)
j = 0
count = 0
#list_4 = []
#define list_4, which is "third list"
# while j < 9:
#     if list_1[j] == list_2[j]:
#         list_4.insert(j, list_1[j])
#         j += 1
#     j += 1
#
# #define if exists duplicates in list
# k = 0
# while k < len(list_4):
#     if list_4.count(list_4[k]) > 1:
#         list_4.remove(list_4[k])
#         k += 1
#         count += 1
#     k += 1
# k += 1
#
# if list_4 == []:
#     print("There is no commom integers")
# else:
#     print(list_4)
list_3 = []
list_4 = {}
while j < 9:
     if list_1[j] == list_2[j]:
         list_3.insert(j, list_1[j])
         list_4 = set(list_3)
     j += 1

if list_4 == {}:
     print("There is no commom integers")
else:
     print(list_4)
