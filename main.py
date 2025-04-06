import random

n=random.randint(1,100)
a=-1
guess=0
while(a!=n):
    guess +=1 
    a=int(input("Guess the number(between 1-100 ): "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")

print(f"You guessed the correct numbmer {n} in {guess} attempts")