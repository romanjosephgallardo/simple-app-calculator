# pseudocode for simple calculator

def welcome_message():
    print("—" * 50)
    print("Welcome to Simple Calculator App!".center(50, " "))
    print("Let's do some math! :D".center(50, " "))
    print("—" * 50)


def invalid_input_message(invalid_input):
    # Displays a formatted invalid message
    line = "—" * 50
    invalid_message = (f"{line} \n"
                       f"\x1B[3m{invalid_input.center(50)}\x1B[0m \n"
                       f"{line} ")
    print(invalid_message)


def formatted_thank_u_message(thank_u):
    # Displays a formatted thanking message
    line = "—" * 50
    thank_u_message = (f" \n"
                       f"{line}\n"
                       f" \n"
                       f"\033[1m{thank_u.center(50)}\033[0m\n"
                       f" \n"
                       f"{line} ")
    print(thank_u_message)


def format_and_display_result(computed_result):
    # Displays a formatted calculated result for operations
    line = ("—" * 40).center(50)
    calculated_result = (f"\n"
                         f"{line} \n"
                         f"\033[1m{computed_result.center(50)}\033[0m \n"
                         f"{line} "
                         f"\n")
    print(calculated_result)


def get_numbers_input(prompt):
    # Prompts the user to enter a numeric value.
    global number
    while True:
        user_input_number = input(prompt)
        if len(user_input_number) > 10:  # Checks if input exceeds 10 characters.
            invalid_input_message("Maximum length reached (10 characters only).")
            continue
        try:
            #  Converting the input to an integer first if detects no decimal point
            number = int(user_input_number)
            break
        except ValueError:
            #  If conversion to integer fails, try converting to float
            try:
                number = float(user_input_number)
                break
            # Handles a non-numeric input for numbers
            except ValueError:
                invalid_input_message("Invalid input. Enter a proper numeric value.")
            except:
                print("Unexpected error occurred. Exiting the program :( ")
                exit()
    return number


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
            formatted_thank_u_message("Thank you for using Simple Calculator App! :D")
            break

    except ValueError:  # If a user enters other characters
        invalid_input_message("Invalid choice. Please enter a valid number")
        continue
    except:
        print("Unexpected error occurred. Exiting the program :( ")
        exit()

    # Ask user to input two numbers
    first_number = get_numbers_input(">>> Enter your first number: ")
    second_number = get_numbers_input(">>> Enter your second number: ")

    # Display the result
    if chosen_option == 1:
        result = first_number + second_number
        format_and_display_result(f"{first_number} + {second_number} = {result}")
    elif chosen_option == 2:
        result = first_number - second_number
        format_and_display_result(f"{first_number} - {second_number} = {result}")
    elif chosen_option == 3:
        result = first_number * second_number
        format_and_display_result(f"{first_number} × {second_number} = {result}")
    elif chosen_option == 4:
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            invalid_input_message("Error: Cannot divide by zero.")
            continue
        else:
            format_and_display_result(f"{first_number} ÷ {second_number} = {result:.2f}")

    # Ask user again if they want to try again
    while True:
        print(">>> Do you want to continue? \n"
              "    (a) Yes   (b) No")
        try:
            try_again = str(input(">>> Choose an option (a/b): "))
            # If yes, repeat the process
            if try_again.lower() == 'a':
                print("-" * 50)
                break
            # If no, display "Thank you" and exit the program.
            elif try_again.lower() == 'b':
                formatted_thank_u_message("Thank you for using Simple Calculator App! :D")
                break
            # If a user enters other characters without on the given option
            if try_again not in ('a', 'b'):
                invalid_input_message("Invalid choice. Please enter a valid letter")
                continue
        except:
            print("Unexpected error occurred. Exiting the program :(. ")
            exit()

    if try_again == "b":  # Checks if 'b' was pressed in the inner loop
        exit()
