from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
userpoints = 0
computerpoints = 0
while userpoints < 3 and computerpoints < 3:
    user = input("Rock, Paper, Scissors?")
    if user == computer:
        print("It's a tie!")
    elif user == "Rock":
        if computer == "Paper":
            computerpoints += 1
            print("You lost!", computer, "beats", user)
        else:
            userpoints += 1
            print("You won!", user, "beats", computer)
    elif user == "Paper":
        if computer == "Scissors":
            computerpoints += 1
            print("You lost!", computer, "beats", user)
        else:
            userpoints += 1
            print("You won!", user, "beats", computer)
    elif user == "Scissors":
        if computer == "Rock":
            computerpoints += 1
            print("You lost!", computer, "beats", user)
        else:
            userpoints += 1
            print("You won!", user, "beats", computer)
    print("Current score You:",userpoints, "Computer:",computerpoints)






