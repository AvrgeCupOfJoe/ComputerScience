from __future__ import print_function
import random

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    The code below asks to guess a randomly selected winner from a defined pool.
    '''
    winner = random.choice(players) 

    ####
    # The code below prints the sentence "Guess which of these people won the lottery: Amy, Bill, Cathey, Dale"
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # this counts how many players are left to put commas
        print(p+', ', end='')
    print(players[len(players)-1]) # this prints the player at which the code is at

    ####
    # This code compares the input to the random winner and if the winner is not the guess then it asks to guess again then names how many times you have guessed
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
    
def goguess():
    
    answer = int(random.choice([1,1,20]))
    
    print('I have a number between 1 and 20 inclusive.')
    print('Guess:')
    
    guess = 0
    guessnumber = 1
    while guess != answer:
        guess = raw_input()
        if guess > answer:
            print(str(guess), 'is too high.')
            guessnumber += 1
        if guess < answer:
            print(str(guess), 'is too low')
            guessnumber += 1
        if guess == answer:
            print('Right! My number is', answer, '!' 'You guessed in', guessnumber, 'guesses!')