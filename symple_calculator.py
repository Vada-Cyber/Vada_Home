print("\n Symple Calculator \n")

continue_calculation = "yes"


     
while True:
        
    enter_number_1 = float(input("First_number is: "))
    enter_operation = input("Enter_operation: ")
    enter_number_2 = float(input("Second_number is: "))


    if enter_operation == "*":
            print(enter_number_1 * enter_number_2)
    elif enter_operation == "/":
                print(enter_number_1 / enter_number_2)
    elif enter_operation == "+":
            print(enter_number_1 + enter_number_2)
    elif enter_operation == "-":
            print(enter_number_1 - enter_number_2)
    else:
            print("Wrong_Operator")
         
    continue_calculation = input(f"continue_calculation ? (yes/no): ").lower()

    if continue_calculation != "yes" and continue_calculation != "y":
        print("End of Calculations")
        break


    # if continue_calculation =="no":
  # break




