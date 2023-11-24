def binomial(n, k)
    def fact(m):
        res, i = 1, 1
        while i <= m:
            res *= i
            i += 1
        return res
    return fact(n) / (fact(k) * fact(n - k))
