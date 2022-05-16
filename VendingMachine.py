def get_vending_machine_result():
    num = int(input("Enter a number :"))
    i = -1
    notes_list = [1, 2, 5, 10, 50, 100, 500, 1000]
    total_no_of_notes = 0
    vending_result = {}

    while i >= -8:
        if num // notes_list[i] > 0 and num > 0:
            num1 = num // notes_list[i]
            num = num % notes_list[i]
            vending_result[str(notes_list[i])] = num1
            total_no_of_notes += num1
        i = i - 1

    vending_result["Total Number of Notes"] = total_no_of_notes
    for i in vending_result:
        print(i + " " + str(vending_result.get(i, -1)))
    return vending_result


if __name__ == '__main__':
    print("Enter money: ")
    get_vending_machine_result()
