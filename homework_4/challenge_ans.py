#input_number = input(f"intut number = ")

odd_numbers = []
seven_divisible_numbers = []
i = 0

while True:

    num = input("input number = ")
    i += 1
    sum_1 = 0
    sum_7 = 0

    if num == "done".lower():
        print("finished")
        break
    elif num.isdecimal() == False:
        print("enter valid number")
        continue
    elif int(num) % 2 != 0 and int(num) % 7 != 0:  # Necessary condition
        print("odd number")
        odd_numbers.append(int(num))
        print(f"odds list : {odd_numbers} ")
    elif int(num) % 7 == 0:
        print("seven_divisible_numbers")
        seven_divisible_numbers.append(int(num))
        print(f"seven_divisible list : {seven_divisible_numbers} ")
    else: 
        print("enter  number") 
        continue

sum_1 = sum(odd_numbers)
sum_7 = sum(seven_divisible_numbers)  

print(i)


print(f"{odd_numbers =} ")
print(f"{seven_divisible_numbers =} ")
print(f"sum of odd_numbers is : {sum_1} ")
print(f"sum of seven_divisible_numbers is : {sum_7} \n ")

        


        

