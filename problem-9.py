#fibanocie series using while loop


def fibonacci_while_loop(n):

    if n <= 0:
        return []
    series = []
    a, b = 0, 1
    count = 0
    while count < n:
        series.append(a)

        a, b = b, a + b
        count += 1
    return series


