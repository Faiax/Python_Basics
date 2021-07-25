
name = input(" Please enter your name: ")
print(" Hello " + name)
age = int(input("How old are you, {}?  ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the Box")
else:
    print("Please come back in {0} years".format(18 - age))
    print("Then you can vote")

print("please guess a number between 1 and 10: ")
guess  = int(input())

if guess <5:
    print("please guess higher")
    guess = int(input())
    if guess == 7:
        print("well done, you have guessed correctly.")
    else:
        print(" sorry, you have not guessed correctly.")
elif guess >6:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("well don, you have guessed it")
    else:
        print("sorry you have not guessed correctly")
else:
    print("you got if for first time")












