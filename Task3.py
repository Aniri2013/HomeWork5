lst = [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]
result = [x for y in lst for x in y]
result = list(filter(lambda x: x > 0, result))
serednya = sum(result)/len(result)
print(serednya)
