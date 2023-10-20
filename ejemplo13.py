import math
digitos = lambda n: 1 if n < 10 else 1+digitos(n//10)
digitos_iter = lambda n , acc : acc if n < 0 else digitos_iter(n//10, 1+acc)
