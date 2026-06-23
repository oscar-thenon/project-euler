from random import randrange

C = 40 # Number of squares
squares = [0]*C # Occurrences of each squares
pos = 0 # Current position
cccards = {0:0,1:10} # CC cards movements
cccardsindex = 0 # CC cards index
chcards = {0:0,1:10,2:11,3:24,4:39,5:5} # CH cards movements
chcardsindex = 0 # CH cards index
db1,db2 = False,False # If two last throws were doubles
N = 10**7 # Number of throws

def special(): # G2J, CC or CH
    global pos, cccardsindex, chcardsindex
    
    if (pos == 30): # G2J
        pos = 10
        
    elif (pos == 2) or (pos == 17) or (pos == 33): # CC
        if cccardsindex < 2:
            pos = cccards[cccardsindex]
        cccardsindex = (cccardsindex+1)%16
        
    elif (pos == 7) or (pos == 22) or (pos == 36): # CH
        if chcardsindex < 6: # Go to a specific case
            pos = chcards[chcardsindex]
        elif (chcardsindex == 6) or (chcardsindex == 7): # Next R
            while (pos%10 != 5):
                pos = (pos+1)%C
        elif (chcardsindex == 8): # Next U
            while (pos != 12) and (pos != 28):
                pos = (pos+1)%C
        elif (chcardsindex == 9): # Go back 3 squares
            pos -= 3
            special() # It's possible that we land on a special square again
        chcardsindex = (chcardsindex+1)%16

def move(): # We throw dice and do a move
    global db1,db2,pos
    d1,d2 = randrange(1,5),randrange(1,5)
    db3 = (d1 == d2)
    if db1 and db2 and db3: # 3 consecutive doubles
        pos = 10
        db1,db2 = False, False # We restart
    else:
        # Updating doubles
        db1 = db2
        db2 = db3
        # Moving
        pos = (pos+d1+d2)%C
        # Checking if we are on a special square
        special() 
    # Incrementing the square we are on
    squares[pos] += 1
            
for i in range(N):
    move()
    
for s in squares:
    print(s) # Displaying squares