#!/usr/bin/env python
import random

'''\
 Rock, paper, scissors, also know as roshambo, is a simple child's game that is 
 frequently used to settle disputes. In the game, a rock breaks the scissors, 
 the scissors cut the paper, and the paper covers the rock. Each option is 
 equally likely to prevail over another. If the players choose the same object 
 a draw is declared and the game is repeated until someone prevails. For more 
 information than you ever thought it was possible to collect about rock, 
 paper, scissors, check out the Web page of the World RPS Society.

In this computerized version the human player competes against the computer 
which chooses a rock, paper, or scissors randomly. The game proceeds for set 
number of rounds at which time the final tally is displayed. 
Solutions with fewer numbers of if statements are considered more "elegant."

source:http://openbookproject.net/pybiblio/practice/\
'''


def calc_winner(user, computer):
    '''\
    Take an input of 'r', 'p' or 's' from both the computer and the user and
    compute the victor
    
    :param user: User's input as 'r', 's', or 'p'
    :type user: character
    :param computer: Computer's input as 'r', 's', or 'p'
    :type computer: character
    :returns: -1 for computer voctpry, 1 for user victory, 0 for a draw
    :rtype: int\
    '''
    if user == computer:
        return 0

    if ((ord(user) > ord(computer) and user != 'p') or
            (user == 'p' and computer == 's')):
        return -1

    return 1


def main():
    '''
    Play a game of Rock, Paper, Scissors with the computer and specify the
    number of rounds that you wish to play
    '''

    # Build string references and result text
    choices = ['r', 'p', 's']
    choice_names = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    results = {0: '\nThe user chose {0} the computer chose {1}'
               '\n\tThe result is a draw',
               1: '\nThe user chose {0} the computer chose {1}'
               '\n\tThe user wins this round!',
               -1: '\nThe user chose {0} the computer chose {1}'
               '\n\tThe computer wins this round!'
               }

    computer_wins = 0
    user_wins = 0
    rounds = int(input('Please enter the number of rounds: '))

    # Start game loop
    for i in range(rounds):
        # Take input from players and decide on the winner
        user_choice = input(
            'Please choose (R)ock, (P)aper or (S)cissors: ').lower()[0]
        computer_choice = random.choice(choices)
        winner = calc_winner(user_choice, computer_choice)
        if winner == -1:
            computer_wins += 1

        elif winner == 1:
            user_wins += 1

        print(results[winner].format(choice_names[user_choice],
                                     choice_names[computer_choice]))
        print('The Scores are\n\t'
              'User: {0}    Computer: {1}\n'.format(user_wins,
                                                    computer_wins))

    # Decide on the winner
    if computer_wins > user_wins:
        print('The computer has bested you in this battle of wits :(')

    elif computer_wins < user_wins:
        print('A winner is you!')

    else:
        print('The overall result is a draw')
        rematch = input('Rematch? (y/n) ').lower()[0]
        if rematch == 'y':
            main()


if __name__ == '__main__':
    main()
