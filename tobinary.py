def to_binary(decimal_value):
    binary_value = []

    s = ''
    while decimal_value >= 1:
        binary_value.append(decimal_value % 2)
        decimal_value = decimal_value // 2

    for i in range(1, len(binary_value) + 1):
        s = s + str(binary_value[-1 * i])

    leftpadding_zeros = s.zfill(4)
    return leftpadding_zeros


if __name__ == '__main__':
    decimal_value = float(input("Enter your Decimal number: "))
    a = to_binary(decimal_value)
    print(a)
