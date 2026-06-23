from math import inf

N = 80 # Length of the matrix
mat = [] # The matrix

""" Importing matrix """
def line_to_list(ln):
    ls = ln.split(',')
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    return ls
f = open("pj082_matrix.txt","r")
for i in range(N):
    mat.append(line_to_list(f.readline()))
f.close()

def updating(x,y,v):
    """ Updating a cell """
    newv = min(gridv[x][y],mat[x][y]+v)
    gridv[x][y] = newv
    if (x,y) in valuescoo:
        i = valuescoo.index((x,y))
        values[i] = newv
    else:
        valuescoo.append((x,y))
        values.append(newv)

def step():
    global nt
    v = min(values)
    vi = values.index(v)
    x,y = valuescoo[vi][0],valuescoo[vi][1]
    gridt[x][y] = True
    values.pop(vi)
    valuescoo.pop(vi)
    if (x > 0) and not gridt[x-1][y]: # Up
        updating(x-1,y,v)
    if (x < N-1) and not gridt[x+1][y]: # Down
        updating(x+1,y,v)
    if (y < N-1) and not gridt[x][y+1]: # Right
        updating(x,y+1,v)

ans = inf    

for x in range(N):
    """ Setting grids """
    # gridv : optimal path values, gridt : is the optimal reached on this cell
    gridv,gridt = [], [] 
    # Setting gridv and gridt
    linf,lt = [inf]*N, [False]*N
    for i in range(N):
        gridv.append(linf.copy())
        gridt.append(lt.copy())

    """ Setting values """
    firstvalue = mat[x][0]
    gridv[x][0] = firstvalue
    values = [firstvalue] # Current non-infinity values to compare
    valuescoo  = [(x,0)] # Coordinates of these
    
    """ Processing """
    for i in range(N**2):
        step()
    
    """ Updating global min if necessary """
    for k in range(N):
        minpath = gridv[k][N-1]
        if minpath < ans:
            ans = minpath
    
print("Answer is", ans)