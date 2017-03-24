from   __future__ import print_function
if raw_input('One character: ') == '!':
    print('Wow', end='!')

def how_eligible(essay):
    rating = 0
    char =''
    for char in essay:
        if char == '?':
            rating = rating + 1
        if char == '"':
            rating = rating + 1
        if char == ',':
            rating = rating + 1
        if char == '!':
            rating = rating + 1
    
    return rating