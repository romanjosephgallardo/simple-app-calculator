# pseudocode for simple calculator

def welcome_message():
    print("—" * 50)
    print("Welcome to Simple Calculator App!".center(50, " "))
    print("Let's do some math! :D".center(50, " "))
    print("—" * 50)


def invalid_input_message(invalid_input):
    line = "—" * 50
    invalid_message = (f"{line} \n"
                       f"\x1B[3m{invalid_input.center(50)}\x1B[0m \n"
                       f"{line} ")
    print(invalid_message)


# Ask user to choose from four math operations
welcome_message()
while True:
    print(">>> What would you like to do? \n"
          " 1. Addition (+) \n"
          " 2. Subtraction (-) \n"
          " 3. Multiplication (×) \n"
          " 4. Division (÷)\n"
          " 5. Exit ")

    try:
        chosen_option = int(input(">>> Choose an option: "))
        if chosen_option not in range(1, 6):  # Validation if user enters other numbers
            invalid_input_message("Invalid choice. Enter a number from 1 to 5 only.")
            continue
        if chosen_option == 5:
            print("Thank you for using Simple Calculator App! :D")
            break

    except ValueError:  # If a user enters other characters
        invalid_input_message("Invalid choice. Please enter a valid number")
        continue

    # Ask user to input two numbers
    try:
        first_number = int(input(">>> Enter your first number: "))
        second_number = int(input(">>> Enter your second number: "))
    except ValueError:
        invalid_input_message("Invalid input. Please enter numeric values only.")
        continue

    # Display the result
    if chosen_option == 1:
        print(f"The sum is: {first_number + second_number}")
    elif chosen_option == 2:
        print(f"The difference is: {first_number - second_number}")
    elif chosen_option == 3:
        print(f"The product is: {first_number * second_number}")
    elif chosen_option == 4:
        try:
            print(f"The quotient is: {first_number / second_number}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            continue

    # Ask user again if they want to try again
    while True:
        print(">>> Do you want to continue? \n"
              " (a) Yes      (b) No")
        try:
            try_again = str(input(">>> Choose an option (a/b): "))
            # If yes, repeat the process
            if try_again.lower() == 'a':
                print("-" * 50)
                break
            # If no, display "Thank you" and exit the program.
            elif try_again.lower() == 'b':
                print("Thank you for using Simple Calculator App! :D")
                break
            # If a user enters other characters without on the given option
            if try_again not in ('a', 'b'):
                invalid_input_message("Invalid choice. Please enter a valid letter")
                continue
        except:
            print("Unexpected error. Exiting the program.")
            exit()

    if try_again == "b":  # Checks if 'b' was pressed in the inner loop
        exit()
