def temp_conv_celsius_to_fahrenheit():
    c = float(input("Enter temperature in Celsius to convert in Fahrenheit °C: "))
    f = (c * 9 // 5) + 32
    print("Fahrenheit is :", f, "°F")


def temp_conv_fahrenheit_to_celsius():
    f = float(input("Enter temperature in Fahrenheit  to convert in Celsius °F: "))
    c = (f - 32) * 5 // 9
    print("Celsius is :", c, "°C")


def main():
    temp_conv_celsius_to_fahrenheit()
    temp_conv_fahrenheit_to_celsius()


if __name__ == '__main__':
    main()
