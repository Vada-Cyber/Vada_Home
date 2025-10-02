print("\n Guess the Number")
iterations = 0

while True:
    iterations += 1
    enter_number = int(input("\n Input_value is: "))
    print(f"\n Iteration {iterations}: Generated {enter_number}")
    if enter_number == 50:
        print(f"\n✓ Found 50! It took {iterations} iterations.")
        break
    elif enter_number >=40 and enter_number < 50:
        print(f"\n iterations : {iterations} , You're_close, But_Low")
    elif enter_number < 40 :
        print(f"\n iterations : {iterations} , Too_low")
    elif enter_number >50 and enter_number <= 60:
        print(f"\n iterations : {iterations} , You're_close, But_High")
    else:
        print(f"\n iterations: {iterations}. Too_High")
print(f"\n Total iterations: {iterations} \n67")
if iterations == 1:
    print (" You're Lucky! \n")







