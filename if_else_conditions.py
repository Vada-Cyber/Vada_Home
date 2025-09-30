balance  = 10
cocktail_price = 14

if balance <14:
    print(f"balance: {balance} Euro")
    print("Transaction Faild, Insufficiant funds!")
else:
    print(f"balance: {balance} Euro")
    print("ok, take your cocktail")


balance_2 = input(f"enter money amount: ")
cocktail_price = 14

if balance_2 < cocktail_price:
    print(f"balance_2: {balance_2} Euro")
    print("Transaction Faild, Insufficiant funds!")
else:
    print(f"balance_2: {balance_2} Euro")
    print("ok, take your cocktail")