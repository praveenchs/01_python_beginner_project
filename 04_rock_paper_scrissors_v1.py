""" Create a game for Rock,Scissors and Paper. Collect input from 2 players and decide who is the winner"""


# collect user input 
player1_input = input("Player1 , choose between rock,scissors or paper: ")
player2_input = input("Player2 , choose between rock,scissors or paper: ")


# validate user input is either rock,scissors or paper . If not throw error .
# Create a list or set of valid input and check if the user input matches the list .
# "not in" ensures all invalid inputs are caught , where as "in" can be ambigious and might miss unexpected inputs . Defensive programming practices 
def validate_input():
    input_list = ["rock", "scissors", "paper"]

    if player1_input not in input_list or player2_input not in input_list:
        print("Wrong input, try again !!! ", input_list)
        return False
    else:
        return True
        
# Always seperate logic from data .  Function validate_input handles data , while who_win is the main logic for the game .
# start with most obvious thing and move on towards ambigious part .
# most obvious logic is that if both inputs are same (use if) , then we go for core logic of the game (use elif) ending with all conditions (else) which does not meet either of the statement 
def who_win():
    if player2_input == player1_input:
        print("Its a tie , try again !!!")

    elif player1_input == "rock" and player2_input == "scissors" or player1_input == "scissors" and player2_input == "paper" or player1_input == "paper" and player2_input == "rock" :
        print("Player1 Wins")

    else:
        print("Player2 Wins !!!")


# this function brings together the data and game logic
# Here we make sure to pass data to game logic only if it is true .
def play():
    if validate_input():
        who_win()

# finally we call the main function 
play()

