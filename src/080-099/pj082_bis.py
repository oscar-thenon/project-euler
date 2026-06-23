from math import inf

class Node:
    def __init__(self,x=0,y=0,weight=inf):
        self.x = x
        self.y = y
        self.w = weight
        
edges = dict()

mat = [[131,673,234,103,18],
       [201,96,342,965,150],
       [630,803,746,422,111],
       [537,699,497,121,956],
       [805,732,524,37,331]]

N = 5

def disp_node(N):
    print("("+str(N.x)+","+str(N.y)+","+str(N.w)+")")

def disp_tab(t,N):
    for i in range(N):
        for j in range(N):
            disp_node(t[i][j])
        print()

nodes = []
for i in range(N):
    nodes.append([0]*N)
for i in range(N):
    for j in range(N):
        nodes[i][j] = Node(i,j)
        
for i in range(N):
    for j in range(N):
        edges[nodes[i][j]] = []
        if i > 0: # Up
            edges[nodes[i][j]].append(nodes[i-1][j])
        if i < N-1:
            edges[nodes[i][j]].append(nodes[i+1][j])
        if j < N-1:
            edges[nodes[i][j]].append(nodes[i][j+1])
            
    
