def golf(number):
    return iter(i for i in range(number + 1, 986899) if str(i) == ''.join(reversed(str(i))) and all((i % j != 0 for j in range(2, i)))).next()
