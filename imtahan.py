try:
    for x in range(6):
        number = int(input("Please enter your number: "))
        choosen = input("Please enter your choosen(+,-)")
        if choosen == "+":
            print(number + number)
        else:
            print(number-number)
except ValueError:
    print("Value not is . Please true value ")
