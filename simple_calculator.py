# pseudocode for simple calculator

def welcome_message():
    line = "—" * 50
    title = "Welcome to Simple Calculator App!"
    subtitle = "Let's do some math! :D"
    print(line)
    print(title.center(50, " "))
    print(subtitle.center(50, " "))
    print(line)


def invalid_choice_message(invalid_choice):
    line = "—" * 50
    invalid_message = (f"{line} \n"
               f"\x1B[3m{invalid_choice.center(50)}\x1B[0m \n"
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
            invalid_choice_message("Invalid choice. Enter a number from 1 to 5 only.")
            continue
        if chosen_option == 5:
            print("Thank you for using Simple Calculator App! :D")
            break

    except ValueError:  # If a user enters other characters
        print("Invalid choice. Please enter a valid number")
        continue

    # Ask user to input two numbers
    try:
        first_number = int(input(">>> Enter your first number: "))
        second_number = int(input(">>> Enter your second number: "))
    except ValueError:
        invalid_choice_message("Invalid input. Please enter numeric values only.")
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
    print(">>> Do you want to continue? \n"
          " (a) Yes      (b) No")
    try:
        try_again = str(input(">>> Choose an option (a/b): "))

        # If yes, repeat the process
        if try_again == 'a':
            continue
        # If no, display "Thank you" and exit the program.
        elif try_again == 'b':
            print("Thank you for using Simple Calculator App! :D")
            exit()
        if try_again not in ('a', 'b'):
            invalid_choice_message("Invalid choice. Please enter a valid letter")
            continue
    except:
        exit()
