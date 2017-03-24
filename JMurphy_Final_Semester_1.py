def voting_age(age):
    VOTE_AGE = 18
    if age < VOTE_AGE:
        print 'No,', age, 'is NOT old enough to vote.'
    else:
        print 'Yes,', age, 'is old enough to vote.'

def Movies(movie):
    Good_movies = ['Batman_Begins','Captain_America','Wolverine','Star_Wars_EmpireStrikesBack']
    Bad_movies = ['Spiderman','Green_Lantern','Howard_the_duck','Mars_attacks','Star_Wars_PhantomMenace']
    Questionable_movies = ['Batman_vs_Superman','Daredevil','Hulk']
    
    if movie in Good_movies:
        print movie, 'is a great movie, you will not be disappointed.'
        if movie is 'Star_Wars_EmpireStrikesBack':
            print 'Dun, dun, dun, dun dun-dun, dun dun-dun'
    else:
        if movie in Bad_movies:
            print movie, 'is a bad movie, you have been warned.'
            if movie is 'Star_Wars_PhantomMenace':
                print 'Now this is Podracing!'
        else:
            if movie in Questionable_movies:
                print movie, '''is questionable, you might like it but don't expect too much.'''
            else:
                print movie, '? No one has ever seen that movie, you might be the first!'

def Battleship(x, y):
    
    secretx, secrety = (10,3)
    if secretx == x and secrety == y:
        print 'Hit! You sunk my battleship'
    else:
            if ( (secretx-x) > 3) or ((secrety-y) > 3):
                print 'Sorry', (x,y),'is a miss!'
            else:
                if ((secretx - x) < 3) or ((secretx - x) == 3) or ((secrety - y) < 3) or ((secrety - y) == 3):
                    print 'Sorry', (x,y),'is a near miss!'
             