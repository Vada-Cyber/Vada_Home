import random
# number_guess = random.randint(1, 100)
# print(number_guess)

# for i in range(5):
#     print(random.randint(1,100))


number_guess_index = 0

while True:

    number_guess = random.randint(1, 100)

    number_guess < 100
    
    number_guess_index += 1
    # print(f"number of iterations was : {number_guess_index}")

    if number_guess == 50:
        print(f" You guessed correct number : {number_guess} ")
        break
    elif number_guess >50:
        print(f" You choose Higher number : {number_guess} ")
    else:
        print(f" You choose Lower number : {number_guess} ")


print(f"number of iterations was : {number_guess_index}")




