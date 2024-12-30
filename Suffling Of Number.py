import random

def main():
    # Get 28 numbers from the user (you can modify this part)
    numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(31)]

    # Shuffle the list of numbers
    random.shuffle(numbers)

    # Print the shuffled list
    print("Shuffled numbers:")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()
