massiv = []
ryad = int(input('Количество рядков: '))
stolb = int(input('Количество столбиков: '))
for i in range(ryad):
    massiv.append([])
    for j in range(stolb):
        massiv[i].append(int(input('Введи число ')))
for i in range(ryad):
    massiv[i].sort()
print(massiv)
