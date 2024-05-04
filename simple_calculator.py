# pseudocode for simple calculator

# Ask user to choose from four math operations
print("Welcome to Simple Calculator App! \n"
      "Let's do some math! :D")
print("What would you like to do? \n"
      " 1. Addition (+) \n"
      " 2. Subtraction (-) \n"
      " 3. Multiplication (×) \n"
      " 4. Division (÷)")
chosen_option = int(input("Choose an option: "))

# Ask user to input two numbers
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number"))

# Display the result
if chosen_option == 1:
    print(f"The sum is: {first_number + second_number}")
if chosen_option == 2:
    print(f"The difference is: {first_number - second_number}")
# Ask user again if they want to try again
# If yes, repeat the process
# If no, display "Thank you" and exit the program.
