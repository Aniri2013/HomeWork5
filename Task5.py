massiv = {}
razm = int(input("Введите количество массивов = "))
dict = {}

for i in range(razm):
    massiv[i] = input("Элементы[" + str(i) + "] = ")
    dict[massiv[i]] = len(massiv[i])

dict = sorted(dict.items(), key=lambda x: x[1],)
for i in range(razm):
    print(dict[i][0])