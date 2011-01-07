def foo():
    x = []

    def bar():
        for i in range(10):
            x.append(i)

    bar()
    print x

foo()
