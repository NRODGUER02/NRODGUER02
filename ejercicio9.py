elem = lambda e,t: False if t == () else \
                   True if e == t[0] else \
                   elem(e, t[1:])
