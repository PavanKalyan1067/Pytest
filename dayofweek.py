def day_of_week(date, month, year):
    d = date
    m = month
    y = year
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7

    if d0 == 0:
        print("Sunday")
    if d0 == 1:
        print("Monday")
    if d0 == 2:
        print("Tuesday")
    if d0 == 3:
        print("Wednesday")
    if d0 == 4:
        print("Thursday")
    if d0 == 5:
        print("Friday")
    if d0 == 6:
        print("Saturday")


if __name__ == '__main__':
    date = int(input("Enter your date: "))
    month = int(input("Enter your month: "))
    year = int(input("Enter your year: "))
    day_of_week(date, month, year)
