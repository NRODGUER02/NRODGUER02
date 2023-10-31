menor_mayor = lambda t, menor, mayor: ((menor, mayor) if t == () else \
                                       menor_mayor_iter(t[1:], min(t[0]),menor), max(t[0], mayor))
