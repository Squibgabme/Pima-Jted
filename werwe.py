import random
print("Hello, please guess a number between 1 and 100")
eric1=0
guess = random.randint(1,100)
while(eric1 != guess):
    eric1 = int(input())
    print("Your Guess was " + str(eric1))
    if (eric1>guess):
        print("You guessed to high")
    if (eric1<guess):
        print("You guessed to low")
    if (eric1==guess):
        print("You win")
#print(guess)


