quita = lambda e, t: t[0] if e == () else \
                     t[1:] if e == t[1:] else \
                     quita (e, t[1:])
