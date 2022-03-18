from webbrowser import get
import numpy as np
import sys
import linecache
print("TRYING")

first = True
rowcount = 0
Os = []
shipsizes = set()
lines = linecache.getlines('1.in')
lines = [x.replace('\n', '') for x in lines]
print(lines)
for line in lines:
    print(line)
    if first:
        n,k = [int(x) for x in line.split(' ')]
        first = False
        grid = np.ones((n,n))
        continue
    if rowcount<n:
        for i,c in enumerate(line):
            if c=='O':
                Os.append((rowcount,i))
            elif c == 'X':
                grid[rowcount,i] = 0
        rowcount += 1
    else:
        shipsizes.add(int(line))
print(grid)
print(shipsizes)

def getPlacements(grid,shipsize): ## returns valid placements in format set((x_a,y_a),(x_b,y_b))
    gridsize = grid.shape[0]
    valid = []
    for i in range(gridsize):
        for c in range(gridsize-shipsize+1):
            if all(grid[i,c:c+shipsize]):
                valid.append(frozenset([(i,c),(i,c+shipsize-1)]))
            if all(grid[c:c+shipsize,i]):
                valid.append(frozenset([(c,i),(c+shipsize-1,i)]))

    return valid

triedplacements = set()
def solveGrid(grid,shipsizes):
    tot = 0
    if not shipsizes:
        return 1
    for shipsize in shipsizes:
        placements = getPlacements(grid,shipsize)
        for placement in placements:
            if placement not in triedplacements:
                subgrid = np.copy(grid)
                if len(placement) == 1:
                    x,y = list(placement)[0]
                    subgrid[x,y] = 0
                else:
                    start, end = placement
                    for x in range(min(start[0],end[0]),max(start[0],end[0])):
                        for y in range(min(start[1],end[1]),max(start[1],end[1])):
                            subgrid[x,y] = 0
                tot +=solveGrid(subgrid,shipsizes.copy().remove(shipsize))
                triedplacements.add(placement)
    return tot

print(solveGrid(grid,shipsizes))
        

getPlacements(grid,2)
def removeOs(grid,shipsizes): ## for each o, generate subgrids with all possible ships going through o with those 
    #spots marked with X and nships, shipsizes - Os.shape sum 
    return

def solveOless(grid,shipsizes):
    return 
