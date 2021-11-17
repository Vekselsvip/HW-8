def my_filter(seq, predicate):
    x = []
    for i in seq:
        x.append(predicate(i))
    return sum(x)


x = [11, 32, 44, 41, 15, 18]
print(my_filter(x, lambda x: x + 3))
