"""
Create a game  rock paper scissors (practice with functions and if statements)
"""

player_1 = input("Player one : ")
player_2 = input("player two : ")


if player_1 == "rock" :
    if player_2 == "scissors":
        print("Player one Win")
    else:
        print("Player two Win")

if player_1 == "scissors" :
    if player_2 == "paper":
        print("player one Wins")
    else:
        print("player two wins")

if player_1 == "paper" :
    if player_2 == "rock":
        print("player one Wins")
    else:
        print("player two wins")


"""else :
    print("Its a tie , try again !!!")"""
