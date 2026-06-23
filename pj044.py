penta = set()

difference = []
somme = []
t = 0
p = 0
c = 0
while 1:
    p += 3*t+1
    if p in somme:
        c += 1
        print difference[somme.index(p)]
        if c == 2:
            break
        
    for old in penta:
        diff = p-old
        if diff in penta:
            difference.append(diff)
            somme.append(p+old)
    penta.add(p)
    t += 1
    