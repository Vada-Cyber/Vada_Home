print("\n Symple Calculator \n")

continue_calculation = "yes"

enter_number_n = 0
enter_number_m = 0
     
# while True:

 
enter_number_m += 1
    # enter_number_n += 1

while True:

        enter_number_n += 1

        enter_number_n = input("\n number is: ")
        if enter_number_n.isdigit():
            enter_number_n = float(enter_number_n)
            break
        else:
            print("wrong symbol 1")
        continue

        while True:
                enter_operation = input("Enter_operation: ")
                if enter_operation not in ("*","/","+","-","%","//","**" ):
                        print("\n Wrong_Operator \n")
                        # continue
                
                enter_number_m = input("\n Second_number is: ")
                if enter_number_m.isdigit():
                        enter_number_m = float(enter_number_m)
                else:
                        print("wrong symbol 2")
                        continue
                        

                if enter_operation == "*":
                        print(enter_number_n * enter_number_m)
                elif enter_operation == "/":
                        print(enter_number_n / enter_number_m)
                elif enter_operation == "+":
                        print(enter_number_n + enter_number_m)
                elif enter_operation == "-":
                        print(enter_number_n - enter_number_m)
                elif enter_operation == "%":
                        print(enter_number_n % enter_number_m)
                elif enter_operation == "//":
                        print(enter_number_n // enter_number_m)
                elif enter_operation == "**":
                        print(enter_number_n ** enter_number_m)
                else:
                        print("Wrong_Operator /n")

                continue_calculation = input(f"continue_calculation ? (yes/no): ").lower()

                if continue_calculation != "yes" and continue_calculation != "y":
                        # continue
                        if continue_calculation !="no" and continue_calculation !="n":
                                print("\n Wrong_Input \n")
                        
                        else:
                                print("\n End of Calculations \n")
                        break






