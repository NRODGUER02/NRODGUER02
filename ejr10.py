x = 4
y = 2
z = 3

primero = x if x < y and x < z else \
          y if y < x and y < z else \
          z

segundo = x if y < x and x < z else \
          y if x < y and y < z else \
          z

tercero = x if y < x and z < x else \
          y if x < y and z < y else \
          z

ordenar1 = (x,y) if x <= y else (y,x)
ordenar2 = (x,z) if x <= z else (z,x)
ordenar3 = (y,z) if y <= z else (z,y)
