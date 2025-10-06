user_input = "5hihoorehqurhbu"
print(len(user_input))

ascii_number = "0123456789"

for c in user_input:
    if c not in ascii_number:
        print("incorrect number")
