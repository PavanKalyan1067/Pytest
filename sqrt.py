def newtons_sqrt_method(number):
    c = number
    t = c

    while abs(t - c / t) > 1e-15 * t:
        t = (t + c / t) / 2
    return t


if __name__ == '__main__':
    numbers = int(input("Enter your number: "))
    a = newtons_sqrt_method(numbers)
    print(a)
