# 1. Створити лист із днями тижня.
# 2. В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# 3. Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict1 = {word:week.index(word)+1 for word in week}
print(dict1)

dict2 = {week.index(word)+1:word for word in week}
print(dict2)
