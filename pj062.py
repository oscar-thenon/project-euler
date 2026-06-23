import sys

di_to_int = {d:ord(d)-48 for d in "0123456789"}

def sort(n):
    """ Sorting n in lexicographic order """
    w = str(n)
    occ = [0]*10
    for d in w:
        occ[di_to_int[d]] += 1
    return tuple(occ)

cubes = {}

p,n,n3 = 1,1,1
while 1:
    while n3 < 10**p:
        w = sort(n3)
        if w in cubes:
            cubes[w][0] += 1
            if cubes[w][0] == 5:
                print("Answer is", cubes[w][1])
                sys.exit()
        else:
            cubes[w] = [1,n3]
        n += 1
        n3 = n**3
    cubes.clear()
    p += 1