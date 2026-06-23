def candidate(x,y,n):
    """ Return True if n can be insert in (x,y) """
    # Line
    if sudoku[x].count(n) == 1:
        return False
    # Row
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    # Region
    xr,yr = (x//3)*3,(y//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[xr+i][yr+j] == n:
                return False
    return True

def solve():
    """ Solve the current sudoku """
    global solved, ans
    
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for n in range(1,10):
                    if candidate(x,y,n):
                        sudoku[x][y] = n
                        solve()
                        if solved:
                            break
                        sudoku[x][y] = 0
                return
            if solved:
                break
        if solved:
            break
    solved = True # This stops the recursion when the solution is found
    ans += 100*sudoku[0][0]+10*sudoku[0][1]+sudoku[0][2]
    
    
def forced_digit():
    """ Find a 'forced' digit. Return False if there isn't one."""
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                c = 0
                lc = 0
                
                for n in range(1,10):
                    if candidate(x,y,n):
                        c = n
                        lc += 1
                        if lc > 1:
                            break
                if lc == 1:
                    sudoku[x][y] = c
                    return True
    return False

def forced_sudoku():
    """ Fills all 'forced' digits """
    while forced_digit():
        pass
    
def convert_line(l):
    """ Converting a line of digits into a list of digits """
    t = []
    for d in l:
        t.append(int(d))
    return t
            
ans = 0

f = open("pj096_sudoku.txt","r")

def aff():
    """ Display the Sudoku for checking """ 
    for i in range(9):
        print(sudoku[i])
    print()

for i in range(50):
    _ = f.readline() # We skip the line "Grid 01" etc
    solved = False
    sudoku = []
    for j in range(9): # Setting the Sudoku
        l = f.readline()
        l = l.rstrip()
        sudoku.append(convert_line(l))
    forced_sudoku()
    solve()


f.close()

print("Answer is", ans)