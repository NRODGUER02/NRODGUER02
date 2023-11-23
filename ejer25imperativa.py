f = open('numeros1.txt', 'r')
lineas1 = list(map(lambda s: int(s.strip()), for s in f.readlines()))
f.close

f = open('numeros2.txt', 'r')
lineas2 = list(map(lambda s: int(s.strip()), for s in f.readlines()))
f.close

lineas = sorted(lineas1 + lineas2)

f = open('resultado.txt', 'w')
f.writelines(str(n) + '\n' for n in lineas)
f.close()
