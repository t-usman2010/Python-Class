import random
x = random.randint(1, 100)

for i in range(5):
    y = int(input("Enter the number: "))
    if x > y:
        print ("The number is Low")
    elif  x < y:
        print("The number is High")
    else:
        x == y
        print("Correct Answer")
print ("The number is: ", x)