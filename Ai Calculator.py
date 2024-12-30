# Calculator Program

def ai_calculator():
    import wolframalpha
    
    while True:
        try:
            text = input("Enter your calculation:  ")
            
            if text.lower() == "exit":
                break
            app_id = "4XAR24-XXH8WT6QQQ"  # Replace with your actual app ID
            client = wolframalpha.Client(app_id)
            query = client.query(text)
            
            if query.results:
                answer = next(query.results).text
                print(f"Answer: {answer}")
            else:
                print("I couldn't understand that. Please try again.")
        except  Exception as e:
            print(f"An error occurred: {e}")


def simple_calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation.lower() == 'exit':
            break
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            print("Result:", num1 + num2)
        elif operation == '-':
            print("Result:", num1 - num2)
        elif operation == '*':
            print("Result:", num1 * num2)
        elif operation == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero.")
        else:
            print("Invalid operation.")

def main():
    while True:
        choice = input("Choose calculator: 1 for Manual Calculations, 2 for Simple Calculator (or 'exit' to quit): ")
        if choice == '1':
            ai_calculator()
        elif choice == '2':
            simple_calculator()
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()