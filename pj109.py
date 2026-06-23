import time
start = time.time()

""" Importing scores """
singles,doubles,trebles = [],[],[]
for s in range(1,21):
    singles.append(s)
    doubles.append(2*s)
    trebles.append(3*s)
singles.append(25) # Bull-eye
doubles.append(50) # Double bull-eye
scores = singles+doubles+trebles

LESSHUNDRED = 0 # Number of checkouts less than a hundred 

def decoding(s,end):
    global LESSHUNDRED
    """ Decoding a set of shots given in a form of stars and bars """
    l = s.split('|')
    score = 0
    for i in range(62):
        score += scores[i]*len(l[i])
    score += end
    if score < 100:
        LESSHUNDRED += 1
        
def combrep(br,sr,end,s=''):
    """ br : remaining bars
    sr : remaining stars
    s : coding the set of shots in a form of starts and bars """
    if (br==0) and (sr==0):
        decoding(s,end)
    else:
        if br != 0: # We can add a bar
            combrep(br-1,sr,end,s+'|')
        if sr != 0: # We can add a star
            combrep(br,sr-1,end,s+'*')
            
""" Main """
            
for d in doubles: # Changing the ending
    for shots in range(3): # Number of shots before the double
        combrep(61,shots,d)

print("Answer is", LESSHUNDRED)
print("\nExecution time :",round(time.time()-start,3))