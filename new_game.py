import random


iterations = 0

while True:
    iterations += 1
    #symple_value = random.randint(1, 100)
    symple_value = int(input(" Input_value is: "))
    print(f"Iteration {iterations}: Generated {symple_value}")
    if symple_value == 50:
        
    if symple_value < 50:
        print(f"iterations : {iterations} , too_low")
    elif symple_value > 50:
        print(f"iterations: {iterations}. too_high")
    else:
        print(f"\n✓ Found 50! It took {iterations} iterations.")
print(f"Total iterations: {iterations}")

