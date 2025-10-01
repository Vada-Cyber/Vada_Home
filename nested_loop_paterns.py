print("Nested loops with break:")
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            print(f"  Found j=1, breaking inner loop")
            break
        print(f"  Inner loop: {j}")