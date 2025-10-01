
iterations = 0

while True:
    iterations += 1
    symple_value = int(input(" Input_value is: "))
    print(f"Iteration {iterations}: Generated {symple_value}")
    if symple_value == 50:
        print(f"\n✓ Found 50! It took {iterations} iterations.")
        break
    elif symple_value < 50:
        print(f"iterations : {iterations} , too_low")
    else:
        print(f"iterations: {iterations}. too_high")
print(f"Total iterations: {iterations}")
if iterations == 1:
    print ("You're Lucky")







