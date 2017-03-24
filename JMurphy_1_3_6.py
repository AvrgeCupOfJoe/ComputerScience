# Mr. Schaeffer's sample code

from __future__ import print_function
import random

def roll_two_dice():
    intDie1= random.randint(1,6)
    intDie2= random.randint(1,6)
    
    return intDie1 + intDie2

def guess_letter():
    tupAlpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    strChar = random.choice(tupAlpha)
    
    return strChar