cont = lambda x: x
cuantos = lambda e, t: cont(-1) if t == () else \
                       cont(0) if e == t[0] else \
                       cuantos (e, t[1:])
