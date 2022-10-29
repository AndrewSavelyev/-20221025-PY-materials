# print(1<2)
#
# print(True is False)
# print(True is True)
#
# bool = "this is bool"
# print(bool)
#
# # True = 1
#
# print(True +(True/False))

# print(True & True) # and
# print(True | True) # or

# a = 1
# # a += 5
# a = a + 5
# print(a)
#
# x1 = 1
# x2 = 1
#
# y1 = "Hello"
# y2 = "Hell"
# # y2 = y2 + "o"
# y2 += "o"
# print(x1 is x2)
# print(y1 is y2)

# num = -1
#
# if num > 3:
#     print("hi from if")
# elif num < 0:
#     print("num < 0")
#     if num == -1:
#         print("num = -1")
# else:
#     print("else")
# print("always")

# s = "qehfbkv"
# # 0 1 2 3 4 5 6
# for i in range(0,len(s)):
#     print(i)

# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Input user for their salary and year of service and print the net bonus amount.

salary = 2000
year_of_serv = 8
bonus = 0.05

if year_of_serv > 5:
    new_salary = salary*(1+bonus)
    print("New salary is: ", new_salary)
else:
    print("No bonus for you! Your salary still: ", salary)

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

grade = 65

if grade >= 80:
    print("You got A")
elif grade >= 60:
    print("You got B")
elif grade >= 50:
    print("You got C")
elif grade >= 45:
    print("You got D")
elif grade >= 25:
    print("You got E")
else:
    print("You got F")

# print all letters except 'e' and 'o' in "Hello" word, use while

word = "Hello"
i = -1
while i < len(word)-1: # H e l l o
    i += 1
    if word[i] == 'e' or word[i] == 'o':
        continue
    print(word[i])






























