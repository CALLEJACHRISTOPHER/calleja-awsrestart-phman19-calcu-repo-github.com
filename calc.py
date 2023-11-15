import os
count = 1

# Clear screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_not_a_number(number):
    if not number.isdigit():
        # loop until the input is a valid number
        while True:
            clear_screen()
            choice = input("Enter a valid number : ")
            if not choice.isdigit():
                 print("Not a Valid Number")
            else:
                # return the valid number
               return choice
    else: 
        # if the value is a valid number just return it to the main loop
        return number
    
    
def is_not_a_number_and_not_zero(number):
    if not number.isdigit() or int(number) == 0:
        # loop until the input is a valid number
        while True:
            clear_screen()
            choice = input("Enter a valid number : ")
            if not choice.isdigit() or int(choice) == 0:
                 print("Not a Valid Number")
            else:
                # return the valid number
               return choice
    else: 
        # if the value is a valid number just return it to the main loop
        return number

def loopAgain():
    # get the user input, if the user wants to go again
    print("1. Go again")
    print("2. End session")
    userInput = input("Select the number of Operation you want to do: ")
    # return 1 if the user wants to go again, return 2 if the user wants to end the loop
    if userInput == "1":
        count = 1
        return count 
    else:
        count = 2
        print("Programmed by Christopher Calleja\nProgram End " )
        return count
    
        
    

def calculator_process(choice):
    clear_screen()
    input1 = input("Enter First Number: ")
    #function to check if input 1 is a valid number
    number1 = is_not_a_number(input1)
    
    
    # make the variable a float
    number1 = float(number1)
    if choice <= "3" and choice >= "1":
        # if the operation is not division check the input if it is a valid number
        input2 = input("Enter Second Number: ")
        number2 = is_not_a_number(input2)
        number2 = float(number2)
    elif choice == "4":
        # if the operation is division check if the input is a valid number and not equal to 0
        input2 = input("Enter Second Number: ")
        number2 = is_not_a_number_and_not_zero(input2)
        number2 = float(number2)

    if choice == "1":
        sum = number1 + number2
        print("Sum of {} and {} is {}".format(number1, number2, sum))
        
    elif choice == "2":
        diff = number1 - number2
        print("Difference of {} and {} is {}".format(number1, number2, diff))
      
    elif choice == "3":
        prod = number1 * number2
        print("Product of {} and {} is {}".format(number1, number2, prod))
      
    elif choice == "4":
        quot = number1 / number2
        print("Quotient of {} and {} is {}".format(number1, number2, quot))
       

while count == 1:
    clear_screen()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. End")
    
    choice = input("Select the number of Operation you want to do: ")
    
    if choice <= "4" and choice >= "0":
        calculator_process(choice)
        count = loopAgain()
    elif choice == "5":
        print("Programmed by Christopher Calleja\nProgram End " )
        count = 2
    else:
        clear_screen()
        print("Input valid choice")
