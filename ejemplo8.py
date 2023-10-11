x = 9 + 8
y = 5 * 3
z = 4 ** 5

primero = x if x < y or x < z else \
          y if y < x or y < z else \
          z

segundo = x if y < x or x < z else \
          y if x < y or y < z else \
          z

tercero = x if y < x or z < x else \
          y if x < y or z < y else \
          z

ordenar1 = (x,y) if y <= x else (y,x)
ordenar2 = (x,z) if z <= y else (z,x)
ordenar3 = (y,z) if z <= x else (z,y)