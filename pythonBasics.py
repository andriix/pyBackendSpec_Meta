def sum_of(*args):
    total = 0
    for x in args:
        total += x
    return round(total, 2)


print(sum_of(3, 5, 2.4))


def sum_of_dict(**kwargs):
    total = 0
    for k, v in kwargs.items():
        total += v
    return round(total, 2)


print(sum_of_dict(coffee=2.3, cake=1.5))
