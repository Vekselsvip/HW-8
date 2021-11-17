def pro(predicate=None, firs: int = 1, stop: int = 10):
    for i in range(firs, stop):
        yield predicate(i)


x = [i for i in pro(lambda x: x ** 2, 2)]
print(x)