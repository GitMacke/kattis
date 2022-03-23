
import sys
import numpy as np
import linecache
import time
first = True
rowcount = 0
Os = []
shipsizes = [0 for _ in range(6)]
line = sys.stdin.readline()
nlines = 0
counter = 0
while line:
    counter+=1
    if first:
        n,k = [int(x) for x in line.split(' ')]
        first = False
        grid = np.ones((n,n))
        nlines += n+k
    else:
        if rowcount<n:
            for i,c in enumerate(line):
                if c=='O':
                    Os.append((rowcount,i))
                elif c == 'X':
                    grid[rowcount][i] = 0
            rowcount += 1
        else:
            shipsizes[int(line)] += 1
    if nlines < counter:
        break
    line = sys.stdin.readline()
start = time.time()
def getPlacements(grid,shipsize): ## returns valid placements in format (x_a,y_a,x_b,y_b))
    gridsize = grid.shape[0]
    valid = []
    for i in range(gridsize):
        for c in range(gridsize-shipsize+1):
            if all(grid[i,c:c+shipsize]):
                valid.append((i,c,i,c+shipsize-1))
            if all(grid[c:c+shipsize,i]):
                valid.append((c,i,c+shipsize-1,i))
    return list(set(valid))

def solveGrid(grid,shipsizes):
    tot = 0
    if not any(shipsizes):
        return all([1-grid[o] for o in Os])
    shipsize = np.argmax(shipsizes)
    placements = getPlacements(grid,shipsize)
    if len(placements) == 0:
        return 0
    shipsizes_reduced = shipsizes.copy()
    shipsizes_reduced[shipsize] -= 1
    count = 0
    
    for placement in placements:
        count += 1
        subgrid = np.copy(grid)
        x1, y1 , x2, y2 = placement
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                subgrid[x,y] = 0
        tot += solveGrid(subgrid, shipsizes_reduced)
    return tot

print(solveGrid(grid,shipsizes))
print(time.time()-start)
