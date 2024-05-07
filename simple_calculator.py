# pseudocode for simple calculator

def show_welcome_message():
    print("—" * 50)
    print("Welcome to Simple Calculator App!".center(50, " "))
    print("Let's do some math! :D".center(50, " "))
    print("—" * 50)


def show_invalid_input_message(invalid_input):
    # Displays a formatted invalid message
    line = "—" * 50
    invalid_message = (f"{line} \n"
                       f"\x1B[3m{invalid_input.center(50)}\x1B[0m \n"
                       f"{line} ")
    print(invalid_message)


def show_thank_u_message(thank_u):
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
    maximum_num_of_characters = 10
    global number
    while True:
        user_input_number = input(prompt)
        if len(user_input_number) > maximum_num_of_characters:  # Checks if input exceeds 10 characters.
            show_invalid_input_message("Maximum length reached (10 characters only).")
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
                show_invalid_input_message("Invalid input. Enter a proper numeric value.")
            except:
                print("Unexpected error occurred. Exiting the program :(. ")
                exit()
    return number


def perform_operation(number_1, number_2, operator):
    # Perform the arithmetic operation based on the operator
    global result
    if operator == '+':  # In addition
        result = number_1 + number_2
    elif operator == '-':  # In subtraction
        result = number_1 - number_2
    elif operator == '×':  # In multiplication
        result = number_1 * number_2
    elif operator == '÷':  # In division
        if number_2 == 0:
            format_and_display_result("Error: Cannot divide by zero.")
            return
        else:
            result = number_1 / number_2

    if result.is_integer():
        format_and_display_result(f"{number_1} {operator} {number_2} = {int(result)}")
    else:
        format_and_display_result(f"{number_1} {operator} {number_2} = {result:.3f}")


# Ask user to choose from four math operations
show_welcome_message()
while True:
    print(">>> What would you like to do? \n"
          " 1. Addition (+) \n"
          " 2. Subtraction (-) \n"
          " 3. Multiplication (×) \n"
          " 4. Division (÷)\n"
          " 5. Exit ")

    try:
        chosen_option = int(input(">>> Choose an option (1/2/3/4/5): "))
        if chosen_option not in range(1, 6):  # Validation if user enters other numbers
            show_invalid_input_message("Invalid choice. Enter a number from 1 to 5 only.")
            continue
        if chosen_option == 5:
            show_thank_u_message("Thank you for using Simple Calculator App! :D")
            break

    except ValueError:  # If a user enters other characters
        show_invalid_input_message("Invalid choice. Please enter a valid number.")
        continue
    except:
        print("Unexpected error occurred. Exiting the program :(. ")
        exit()

    # Ask user to input two numbers
    first_number = get_numbers_input(">>> Enter your first number: ")
    second_number = get_numbers_input(">>> Enter your second number: ")

    # Display the result
    if chosen_option == 1:
        perform_operation(first_number, second_number, '+')
    elif chosen_option == 2:
        perform_operation(first_number, second_number, '-')
    elif chosen_option == 3:
        perform_operation(first_number, second_number, '×')
    elif chosen_option == 4:
        perform_operation(first_number, second_number, '÷')

    # Ask user again if they want to try again
    while True:
        print(">>> Do you want to continue? \n"
              "    (a) Yes   (b) No")
        try:
            try_again = str(input(">>> Choose an option (a/b): ")).lower()
            # If yes, repeat the process
            if try_again == 'a':
                print("-" * 50)
                break
            # If no, display "Thank you" and exit the program.
            elif try_again == 'b':
                show_thank_u_message("Thank you for using Simple Calculator App! :D")
                break
            # If a user enters other characters without on the given option
            elif try_again not in ('a', 'b'):
                show_invalid_input_message("Invalid choice. Please enter a valid letter.")
                continue
        except:
            print("Unexpected error occurred. Exiting the program :(. ")
            exit()

    if try_again == "b":  # Checks if 'b' was pressed in the inner loop
        exit()
