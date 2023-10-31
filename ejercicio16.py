rota = lambda n, t: t if n or t == 0 else \
                      rota(n-1, t[1:]+(t[0],))
