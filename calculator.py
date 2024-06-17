def calculator():
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modular Division")
        
        user_input = input("Enter your choice (1/2/3/4/5): ")
        num = ['1', '2', '3', '4', '5']
        
        if user_input in num:
            if user_input == '1':
                print("Answer:", n1 + n2)
            elif user_input == '2':
                print("Answer:", n1 - n2)
            elif user_input == '3':
                print("Answer:", n1 * n2)
            elif user_input == '4':
                if n2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print("Answer:", n1 / n2)
            elif user_input == '5':
                if n2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print("Answer:", n1 % n2)
        else:
            print("Invalid choice! Please enter a valid operation.")
    
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
