def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


# test case
def test():
    
    assert x_or_y(7, 34, 12) == 34

    assert x_or_y(15, 8, 5) == 5


    assert x_or_y(1, 5, 9) == 5


    assert x_or_y(30, 20, 10) == 20

    assert x_or_y(-7, -34, -12) == -12