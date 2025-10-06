outer_counter = 0
while outer_counter < 3:
    print(f"Outer loop iteration: {outer_counter}")
    inner_counter = 0
    while inner_counter < 5:
        print(f"  Inner loop iteration: {inner_counter}")
        if inner_counter == 2:
            print("  Breaking out of inner loop!")
            break  # This breaks out of the inner while loop only
        inner_counter += 1
    print(f"Continuing outer loop after inner loop exit for outer_counter = {outer_counter}")
    outer_counter += 1
print("Program finished.")

