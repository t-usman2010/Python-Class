from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

print("Please wait Programe is starting")

def ai_calculator():
    # Load pre-trained model and tokenizer
    model_name = "microsoft/DialoGPT-medium"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Chat loop
    chat_history_ids = None
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Solver: Goodbye!")
            break

        # Encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

        # Append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids

        # Generate a response
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Decode the response
        bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"Solver: {bot_response}")

def simple_calculator():
    print("Running Code Two")
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
    print("Choose which code to run:")
    print("1. Ai Calculator")
    print("2. Simple Calculator")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        ai_calculator()
    elif choice == '2':
        simple_calculator()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
