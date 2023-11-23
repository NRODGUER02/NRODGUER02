while True:
    try:
        n = int(input('introduzca un numero: '))
        print('El valor introducido es correcto')
        break
    except ValueError:
        print('El dato introducido no es un número')
divisores = 0

i = 1

while i <= n:
    if n % i == 0:
        divisores += 1
    i += 1

if divisores == 2:
    primo = True
else:
    primo = False

if primo:
    print('Es primo')
else:
    print('Es compuesto')

    print('Encantado de conocerte')
    print('Gracias por ejecutar este programa')
