w = 2
f = lambda x, y: 5 + (lambda z: z + 3)(x + y)
r = f(2, 4)
m = (lambda x: x ** 2)(3)