import math
digitos = lambda n: 1 if n < 10 else 1+digitos(n//10)
