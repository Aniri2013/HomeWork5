input_words = str(input('Введи слова через пробел - ')).split(' ')
unical = 0
dict = {}
for item in input_words:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

for word in input_words:
    if (dict[word] == 1):
        unical += 1

print(unical)
