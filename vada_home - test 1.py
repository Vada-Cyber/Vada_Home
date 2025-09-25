PI = 3.14 # all big letters means Constant argument
balance = 100
sandwich = 6
groceries = 50
sandwich_count = 5 #snake_case 
groceries_count = 10

# print("balance")  all comands 
# print(balance)
# print("sandwich")
# print(sandwich)
# print("groceries")
# print(groceries)

print(f"balance: {balance}") # f is formating
print(f"sanwich: {sandwich}")

print(f"I am buying {sandwich_count} that costs {sandwich * sandwich_count} bucks, I have {balance}")
# balance = balance - (sandwich * sandwich_count)
balance -= (sandwich * sandwich_count)
print(f"Now I have {balance} $")

print(f"I am buying {groceries_count} that costs {groceries * groceries_count} bucks, I have {balance}")
balance -+ (groceries * groceries_count)
print(f"Now I have {balance} $ after grocery buying")