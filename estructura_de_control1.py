while True:
    try:
        edad = int(input('Introduzca su edad: '))
        if edad < 25:
            print('¡Que joven!')
            print('Encantado de conocerte')
            print('Gracias por ejecutar este programa')
        elif edad >= 25 and edad <= 40:
            print('Ok')
            print('Encantado de conocerte')
            print('Gracias por ejecutar este programa')
        else:
            print('¡Que mayor!')
            print('Encantado de conocerte')
            print('Gracias por ejecutar este programa')
        break
    except ValueError:
        print('Error')
        print('Encantado de conocerte')
        print('Gracias por ejecutar este programa')
