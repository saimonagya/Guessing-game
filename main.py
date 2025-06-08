import random

print("I'm guessing a number from 1 to 100")
n = int(input("Enter the number:"))
a=random.randint(1,100)
i=0
if(n>a):
    print("Too high")
    i=i+1
elif(n<a):
    print("Too low")
    i=i+1
elif (n==a):
    print(f"Correct! You've guessed the number in {i} attempts.")