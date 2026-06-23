nyear = [] #Normal year#
lyear = [] #Leap year#

# nyear#
for i in range(1,32): #janvier#
    nyear.append(i)
for i in range(1,29): #fevrier#
    nyear.append(i)
for j in range(2): #jusqua juin#
    for i in range(1,32): 
        nyear.append(i)
    for i in range(1,31): 
        nyear.append(i)
for i in range(1,32): #juillet#
    nyear.append(i)
for j in range(2): #jusqua nov#
    for i in range(1,32): 
        nyear.append(i)
    for i in range(1,31): 
        nyear.append(i)
for i in range(1,32): #decembre#
    nyear.append(i)
    
# lyear#
for i in nyear:
    lyear.append(i)
lyear.insert(59,29)

days = [] # tous les numeros de jour

for i in range(1901, 2000): # jusqu'a l'annee 1999
    if (i%4 == 0):
        for j in lyear:
            days.append(j)
    else:
        for j in nyear:
            days.append(j)
for j in lyear: # On rajoute l'annee 2000 qui est leap
            days.append(j)

N = len(days)

c = 0 # Compteur dimanches

for i in range(N):
    c += ((days[i] == 1) and (i%7 == 0)) # Le 1er janvier 1901 etait un mardi

print "Answer is", c
    

    

