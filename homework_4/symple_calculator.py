
print("\n Symple Calculator \n")

continue_calculation = "yes"
enter_number_1 = 0
enter_number_2 = 0

     
while True:
    while True:
        enter_number_1 = input("First number is: ")
        try:
            enter_number_1 = float(enter_number_1)
            break
        except ValueError:
            print("wrong symbol - please enter a valid number")

    while True:
        enter_operation = input("Enter_operation: ")
        if enter_operation in ("*","/","+","-","%","//","**" ):
            break
        else:
            print("\n Wrong_Operator \n")


    while True:
        enter_number_2 = input("Second_number is: ")
        try:
            enter_number_2 = float(enter_number_2)
            break
        except ValueError:
            print("wrong symbol - please enter a valid number")

    if enter_operation == "*":
        print(enter_number_1 * enter_number_2)
    elif enter_operation == "/":
        if enter_number_2 != 0:
           print(enter_number_1 / enter_number_2)
        else:
           print ( " deviation to 0 is restricted ")
    elif enter_operation == "+":
        print(enter_number_1 + enter_number_2)
    elif enter_operation == "-":
        print(enter_number_1 - enter_number_2)
    elif enter_operation == "%":
        print(enter_number_1 % enter_number_2)
    elif enter_operation == "//":
        print(enter_number_1 // enter_number_2)
    elif enter_operation == "**":
        print(enter_number_1 ** enter_number_2)

    while True:
        continue_calculation = input(f"continue_calculation ? (yes/no): ").lower()
        if continue_calculation in ("yes","y"):
            break
        elif continue_calculation in ("no", "n"):
            print ( "End of Calculation \n")
            exit()
        else:
             print("Wrong input - please enter 'yes' or 'no'" )






