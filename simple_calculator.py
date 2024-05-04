# pseudocode for simple calculator

# Ask user to choose from four math operations
print("Welcome to Simple Calculator App! \n"
      "Let's do some math! :D")
try:
    print("What would you like to do? \n"
          " 1. Addition (+) \n"
          " 2. Subtraction (-) \n"
          " 3. Multiplication (×) \n"
          " 4. Division (÷)")
    chosen_option = int(input("Choose an option: "))

    if chosen_option not in range(1, 5):  # Validation if user enters other numbers
        print("Invalid choice. Please enter a number between 1 and 4")
        exit()

except ValueError:  # If a user enters other characters
    print("Invalid choice. Please enter a valid number")
    exit()

# Ask user to input two numbers
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# Display the result
if chosen_option == 1:
    print(f"The sum is: {first_number + second_number}")
if chosen_option == 2:
    print(f"The difference is: {first_number - second_number}")
if chosen_option == 3:
    print(f"The product is: {first_number * second_number}")
try:
    if chosen_option == 4:
        print(f"The quotient is: {first_number / second_number}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# Ask user again if they want to try again
print("Do you want to calculate again? \n"
      " (a) Yes      (b) No")
try_again = str(input("Choose an option: "))

# If yes, repeat the process
if try_again == "a":
    exit()  # will change this part for looping 
# If no, display "Thank you" and exit the program.
else:
    print("Thank you for using Simple Calculator App! :D")
