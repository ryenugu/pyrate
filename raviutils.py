def fib(n):
    """Prints n nubmers of the fib sequence """
    a, b = 0, 1

    for i in range(n + 1):
        yield a
        a, b = b, a + b


def is_multiple(n, m):
    """Returns True if n is a multiple of m"""
    return n % m == 0


def is_even(k):
    """
    returns True if k is even False otherwise : without using modulo divison or multiplication
    """
    return bin(k)[-1] == '0'


def minmax(data):
    """
    find and return min,max as tuple from data list
    """
    minn = maxx = 0
    if len(data) > 1:
        for x in range(1, len(data)):
            if data[x] < data[minn]:
                minn = x
            if data[x] > data[maxx]:
                maxx = x
    return data[minn], data[maxx]
