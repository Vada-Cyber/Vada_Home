import random

print("\n Digital Generator \n")

press_enter = input("Press Enter to generate a random number between 1 and 100 (or type 'exit' to quit): ")

odd_numbers = []
seven_divisible_numbers = []

while True:

    if press_enter.lower() == 'done':
        print("Exiting the program.")
        break
    elif press_enter.isdigit() == False:
        print("Enter a valid input")
        press_enter = input("Press Enter to generate a random number between 1 and 100 (or type 'exit' to quit): ")
        continue
    elif press_enter == "":
        random_number = random.randint(-100, 100)
        print(f"Generated random number: {random_number}")
        press_enter = input("Press Enter to generate another number (or type 'exit' to quit): ")
        if random_number % 2 != 0:
            odd_numbers.append(random_number)
        elif random_number % 7 == 0:
            seven_divisible_numbers.append(random_number)

    else:
        print("Invalid input. Please press Enter to generate a number or type 'exit' to quit.")
        press_enter = input("Press Enter to generate a random number between 1 and 100 (or type 'exit' to quit): ")


