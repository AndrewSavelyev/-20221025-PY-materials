# #Lesson_4 Цикл for-in
# a_list = [1, 2, 3, 4, 5]
# for item in a_list:
#     if item == 10:
#         break
#     print(item)
# print("ok")

#Словники та генератор списку
#Для создания пустого списка используем {}
#Для создания пустого множества- не можем использовать {}
#Почему?
#Множества не имеют четкой последовательности
#Пустое множество создаем через set()

# task_1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
# the number of occurrences as values.

# list = [9, 6, 3, 10]
# print("Number of 6", list.count(6))
# print("Index of fisrt accurance of 6", list.index(6))

sentence1 = "Make a program the has some sentence a string on input and returns a dict containing all unique words as"
sentence2 = "keys and the number of some occurrences as values"
sentence = sentence1 + " " + sentence2
list = sentence.split()
unique = set(list)
print(list)
print(unique)
dict = {}
for word in list:
    if word in unique:
     dict[word] = list.count(word)
print(dict)








