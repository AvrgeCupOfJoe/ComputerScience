# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
import random

# -*- coding: utf-8 -*-
def days():
    ''' For the first for loop day is set to M then runs the print and increments to T and then W and so on. For the second for loop day is set to 5 then runs the print and increments to 6 then 7.
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list
    b = []
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1, 3, 10])]
    b += [random.choice([2, 4, 11])]
    
    for choices in range(5):
        a += [random.choice([1, 3, 10])]
        b += [random.choice([2, 4, 11])]
    plt.hist(a + b)
    plt.show()
    
def roll_hundred_pair():
    die1 = []
    die2 = []
    
    die1 += [random.choice([1, 7, 1])]
    die2 += [random.choice([1, 7, 1])]
    
    for choices in range(100):
        die1 += [random.choice([1, 7, 1])]
        die2 += [random.choice([1, 7, 1])]
    plt.hist(die1 + die2)
    plt.show()
    
def matches(ticket, winners):
    matches = 0 #Total matches in the two tickets
    i = 0 #Counter variable
    for number in ticket: #Runs for each item in "ticket"
        if ticket[i] in winners: #Checks if the "i"th item is in "winner"
                matches += 1 #Adds one to the matching count
        i += 1 #Adds one to the counter variable
    #Repeats until all items in "ticket" are checked
    print (matches) #Prints number of matches