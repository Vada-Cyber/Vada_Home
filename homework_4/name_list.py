def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("FRIEND LIST MANAGER")
    print("="*40)
    print("1. Add a new friend")
    print("2. Remove a friend")
    print("3. Search for a friend")
    print("4. Display all friends (alphabetically)")
    print("5. Exit")
    print("="*40)

def add_friend(friends):
    """Add a new friend to the list"""
    name = input("Enter the name of your friend: ").strip()
    
    if not name:
        print("Error: Name cannot be empty!")
        return
    
    if name in friends:
        print(f"'{name}' is already in your friend list!")
    else:
        friends.append(name)
        print(f"'{name}' has been added successfully!")

def remove_friend(friends):
    """Remove a friend from the list"""
    if not friends:
        print("Your friend list is empty! Nothing to remove.")
        return
    
    name = input("Enter the name of the friend to remove: ").strip()
    
    if not name:
        print("Error: Name cannot be empty!")
        return
    
    if name in friends:
        friends.remove(name)
        print(f"'{name}' has been removed from your friend list.")
    else:
        print(f"'{name}' is not in your friend list!")

def search_friend(friends):
    """Search for a friend in the list"""
    if not friends:
        print("Your friend list is empty!")
        return
    
    name = input("Enter the name to search for: ").strip()
    
    if not name:
        print("Error: Name cannot be empty!")
        return
    
    if name in friends:
        print(f"✓ '{name}' is in your friend list!")
    else:
        print(f"✗ '{name}' is not in your friend list!")

def display_friends_alphabetical(friends):
    """Display all friends in alphabetical order"""
    if not friends:
        print("Your friend list is empty!")
        return
    
    sorted_friends = sorted(friends)
    print("\nYour friends (alphabetically):")
    print("-" * 40)
    for i, friend in enumerate(sorted_friends, 1):
        print(f"{i}. {friend}")
    print(f"\nTotal friends: {len(friends)}")

def get_valid_choice():
    """Get and validate user menu choice"""
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

def main():
    """Main function to run the friend list manager"""
    # Initialize empty friend list
    friends = []
    
    print("Welcome to Friend List Manager!")
    
    while True:
        display_menu()
        choice = get_valid_choice()
        
        if choice == '1':
            add_friend(friends)
        elif choice == '2':
            remove_friend(friends)
        elif choice == '3':
            search_friend(friends)
        elif choice == '4':
            display_friends_alphabetical(friends)
        elif choice == '5':
            print("\nThank you for using Friend List Manager!")
            if friends:
                print(f"Final friend count: {len(friends)}")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

