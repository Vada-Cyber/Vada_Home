import random

print(" \n Press Enter Key or type 'done' to Exit \n")
print("Press Enter to generate")


odd_numbers = []
seven_divisible_numbers = []
i = 0

while True:

    press_enter = input()

    i += 1
    
    

    if press_enter.lower() == "done":
        print("Done, Goodbye\n")
        break
        
        if 
    elif int(press_enter) % 2 != 0 and int(press_enter) % 7 != 0:
        print("odds entered")
        odd_numbers.append(int(press_enter))
    elif int(press_enter) % 7 == 0 :
        print("seven divisible entered")
        seven_divisible_numbers.append(int(press_enter))
        print(f" {press_enter = }")
    else:
        press_enter = random.randint(-1000, 1000)
        print(press_enter)




print(i)
print(f"\n {seven_divisible_numbers =}") 
print(f"\n {odd_numbers =}")        
    

