massiv = {}

m = int(input("Введите столбец = "))
n = int(input("Введите строку  = "))

for i in range(m):
    for j in range(n):
        massiv[i, j] = int(input("massiv [" + str(i) + "][" + str(j) + "] = "))

min = 1
for i in range(m):
    for j in range(n):
        if massiv[i, j] < min:
            min = massiv[i, j]

print(min)