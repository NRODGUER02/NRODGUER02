def fact(n):
    def fact_iter(acc, n):
        if n == 0:
            return acc
        else:
            return fact_iter(n - 1, acc * n)
    return fact_iter(n, 1)

print(fact(5))

# daría un error porque fact_iter no existe en el ámbito global:
print(fact_iter(5, 1))
print('Encantado de conocerte')
print('Gracias por ejecutar este programa')
