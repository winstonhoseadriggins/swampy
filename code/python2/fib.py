def fib(n, d={0:1, 1:1}):
    try:
        return d[n]
    except KeyError:
        d[n] = fib(n-1) + fib(n-2)
        return d[n]


print fib(10)
