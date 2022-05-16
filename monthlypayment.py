def monthly_payment(principle, rate, year):
    P = principle
    R = rate
    Y = year
    n = 12 * Y
    r = R / 12 * 100

    payment = (P * r) / 1 - pow((1 + r), (-1 * n))
    print(payment)


if __name__ == '__main__':
    principle = int(input("Enter your principle Amount: "))
    rate = int(input("Enter your rate: "))
    year = int(input("Enter year: "))

    monthly_payment(principle, rate, year)
