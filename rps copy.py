"""A template for a python script deliverable for INST326.
Driver: Yamlak Shimelis
Navigator: Kai Jung
Assignment: Template INST326
2
Date: 1_24_21
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import sys
import argparse
import os

def determine_winner(p1, p2):
    """Compares handshapes (p1 and p2) of each player and returns which person wins
    arguments:
        p1 (str): handshape of player 1. Must be 'r', 'p', or 's'
        p2 (str): handshape of player 2. Must be 'r', 'p', or 's'
    returns:
        string: which player wins. If none, returns tie
    """
    if p1 == p2:
        return 'tie'
    elif p1 == 'r' and p2 == 's':
        return 'player1'
    elif p1 == 'r' and p2 == 'p':
        return 'player2'
    elif p1 == 's' and p2 == 'r':
        return 'player2'
    elif p1 == 's' and p2 == 'p':
        return 'player1'
    elif p1 == 'p' and p2 == 'r':
        return 'player1'
    elif p1 == 'p' and p2 == 's':
        return 'player2'
    pass

def main(player1_name, player2_name):
    """Prompts players to enter their hand shapes uses determine_winner function
    to print who wins.
    arguments:
        player1_name (str): name of player 1
        player2_name (str): name of player 2
    side effects:
        Prints winning player's name followed by 'wins!'. If tied, prints 'Tie!'
    """
    player1_hand = input("Player 1 please enter your hand shape: ")
    player2_hand = input("Player 2 please enter your hand shape: ")
    winner = determine_winner(player1_hand,player2_hand) 
    if winner == 'player1':
        print(player1_name + ' wins!')
    elif winner == 'player2':
        print(player2_name + ' wins!')
    else:
        print("Tie!")
    pass

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations
    #commence.
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
    parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
    args = parser.parse_args(args_list) #We need to parse the list of command line
#arguments using this object.
    return args
if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
#3
    #It the script is being run as a module, the block of code under this will not be
#executed.
    #If the script is being run natively, the block of code below this will be
#executed.
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments
#to the parse_args function.
    #The returned object is an object with those command line arguments as attributes
#of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ ==
#"__main__":' statement.
    main(arguments.p1_name, arguments.p2_name)