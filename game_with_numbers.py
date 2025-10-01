
iterations = 0

while True:
    iterations += 1
    symple_value = int(input("\n Input_value is: "))
    print(f"\n Iteration {iterations}: Generated {symple_value}")
    if symple_value == 50:
        print(f"\n✓ Found 50! It took {iterations} iterations.")
        break
    elif symple_value >=40 and symple_value < 50:
        print(f"\n iterations : {iterations} , You're_close, But_Low")
    elif symple_value < 40 :
        print(f"\n iterations : {iterations} , Too_low")
    elif symple_value >50 and symple_value <= 60:
        print(f"\n iterations : {iterations} , You're_close, But_High")
    else:
        print(f"\n iterations: {iterations}. Too_High")
print(f"\n Total iterations: {iterations} ")
if iterations == 1:
    print ("\n You're Lucky! \n")







