import random

number_random = 0

# for i in range (1, 50):
    
    
while True:

    number_random = random.randint(1, 100)

    if number_random % 3 != 0:
        print(f"{number_random}")
        continue

    if number_random % 2 == 0:
        continue
            
    else:
        num = int(number_random / 3)
        print(f"Generated Number is : {number_random}, and devidation result is :  {num}")
        break    


