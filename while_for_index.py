# count = 0
# while count < 5:
#     print(count)
#     count += 1  # Increment count by 1


# # Note: this would normally require user input
# answer = "quit"
# while answer != "quit":
#     print("Current answer:", answer)
#     answer = "quit"  # Normally this would be input("Enter 'quit' to exit: ")


    # This pattern is common when requiring continuous user interaction



while True:
    # user_input = input("Type 'exit' to quit: ")
    user_input = input("user_input: ")
    # user_input = "exit"  # Simulating input for documentation
    print("You entered:", user_input)
    if user_input.lower() == 'exit':
        break