x = tuple((x, y) for x in range(1, 10000) for y in range(1, 10000) if x + y == 10000)
y = tuple((x, y) for x in range(1, 10000) for y in range(1, 10000) if x - y == 10000)
a = tuple((x, y) for x in range(1, 10000) for y in range(1, 10000) if x * y == 10000)
b = tuple((x, y) for x in range(1, 10000) for y in range(1, 10000) if x / y == 10000)
suma = x + a
print(suma)
