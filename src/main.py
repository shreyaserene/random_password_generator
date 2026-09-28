from password_generator import generate_password
from strength_analyzer import analyze_password
from validator import check_length


print("================================")
print("          SECUREPASS")
print("   Random Password Generator")
print("================================")


while True:

    print("\n---------- MENU ----------")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n--- Generate Password ---")

        try:
            length = int(input("Enter password length: "))

            if not check_length(length):
                print("\nError: Password length must be at least 8.")
                continue

            password = generate_password(length)

            print("\nGenerated Password:", password)

            print("\nPassword Strength:")
            analyze_password(password)

        except ValueError:
            print("\nError: Please enter a valid number.")

    elif choice == "2":

        print("\nThank you for using SecurePass!")
        print("Goodbye!")

        break

    else:

        print("\nInvalid choice.")
        print("Please enter 1 or 2.")