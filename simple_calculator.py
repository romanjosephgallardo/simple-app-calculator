# pseudocode for simple calculator

# Ask user to choose from four math operations
print("Welcome to Simple Calculator App! \n"
      "Let's do some math! :D")
while True:
    print("What would you like to do? \n"
          " 1. Addition (+) \n"
          " 2. Subtraction (-) \n"
          " 3. Multiplication (×) \n"
          " 4. Division (÷)\n"
          " 5. Exit ")

    try:
        chosen_option = int(input("Choose an option: "))
        if chosen_option not in range(1, 6):  # Validation if user enters other numbers
            print("Invalid choice. Please enter a number between 1 and 4")
            continue
        if chosen_option == 5:
            print("Thank you for using Simple Calculator App! :D")
            break

    except ValueError:  # If a user enters other characters
        print("Invalid choice. Please enter a valid number")
        continue

    # Ask user to input two numbers
    try:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values")
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
    print("Do you want to continue? \n"
          " (a) Yes      (b) No")
    try:
        try_again = str(input("Choose an option (a/b): "))

        # If yes, repeat the process
        if try_again == 'a':
            continue
        # If no, display "Thank you" and exit the program.
        elif try_again == 'b':
            print("Thank you for using Simple Calculator App! :D")
            exit()
        if try_again not in ('a', 'b'):
            print("Invalid choice. Please enter a valid letter")
            continue
    except:
        exit()
