nomer = int(input('введи число: '))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
more_less = input('Введите какие числа считать (больше/меньше):')

while not(more_less == 'больше' or more_less == 'меньше'):
    print("Попытайтесь еще: ")
    more_less = input()
cnt = 0

if more_less == 'больше':
    for i in lst:
        if i> nomer:
            cnt += 1
else:
    for i in lst:
        if i< nomer:
            cnt += 1
print(nomer)
