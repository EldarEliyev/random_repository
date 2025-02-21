try:
    import random
    random_choice = random.choice(["+", "-"])
    for x in range(6):
        number = int(input("Please enter your number: "))
        if random_choice == "+":
            print(number + number)
        else:
            print(number-number)
except ValueError:
    print("No floats. Please enter your integer number: ")
except TypeError:
    print("No type string and float . Please integer:")
except NameError:
    print("No name is")

    

