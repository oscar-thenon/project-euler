from src.fonctions import combl

def diceapp(l):
    dice.append(l)

dice = []
combl(10,6,diceapp) # Generating all possible dices

squares = {'01','04','09','16','25','36','49','64','81'}

def add_numbers(a,b,numbers):
    sa,sb = str(a),str(b)
    numbers.add(sa+sb)
    numbers.add(sb+sa)
    if a == 9:
        numbers.add('6'+sb)
        numbers.add(sb+'6')
    elif a == 6:
        numbers.add('9'+sb)
        numbers.add(sb+'9')
        
    if b == 9:
        numbers.add(sa+'6')
        numbers.add('6'+sa)
    elif b == 6:
        numbers.add(sa+'9')
        numbers.add('9'+sa)

def dice_square(d1,d2):
    """ True if d1 and d2 produce all squares """
    numbers = set()
    
    for a in d1:
        for b in d2:
            add_numbers(a,b,numbers)
            
    numbers = numbers.intersection(squares)
    return len(numbers) == 9
        
ans = 0

for (i,d1) in enumerate(dice):
    for j in range(i+1):
        d2 = dice[j]
        ans += dice_square(d1,d2)
        
print("Answer is", ans)