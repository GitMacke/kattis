
import sys

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
        grid = [[1 for r in range(n)] for c in range(n)]
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
#placementTime = 0
#totStart = time.time()

def calcSingles(grid,nsingles):
    Os_left = sum([grid[o[0]][o[1]] for o in Os])
    if Os_left>nsingles:
        return 0
    nways_to_fill_Os = 1
    for x in range(Os_left):
        nways_to_fill_Os*=nsingles-x
    to_place = nsingles - Os_left
    ans = 1
    spots_left = sum([sum(row) for row in grid])-Os_left
    for x in range(to_place):
        ans*=spots_left-x
    return ans*nways_to_fill_Os

def solveGrid(grid,shipsizes):
    tot = 0
    if not any(shipsizes):
        return all([1-grid[o[0]][o[1]] for o in Os])
    shipsize = max([i for i,x in enumerate(shipsizes) if x != 0])
    if shipsize == 1:
        return calcSingles(grid,shipsizes[1])
    shipsizes[shipsize] -= 1
    for i in range(n):
        for c in range(n-shipsize+1):
            if all(grid[i][c:c+shipsize]):
                for y in range(c,c+shipsize):
                    grid[i][y] = 0
                tot += solveGrid(grid, shipsizes)
                for y in range(c,c+shipsize):
                    grid[i][y] = 1
            vert = [grid[c_i][i] for c_i in range(c,c+shipsize)]
            if all(vert): 
                for x in range(c,c+shipsize):
                    grid[x][i] = 0
                tot += solveGrid(grid,shipsizes)
                for x in range(c,c+shipsize):
                    grid[x][i] = 1
    shipsizes[shipsize] += 1
        
    return tot

tot = 0
if not any(shipsizes):
    tot+=all([1-grid[o[0]][o[1]] for o in Os])
shipsize_0 = max([i for i,x in enumerate(shipsizes) if x != 0])
if shipsize_0 == 1:
    tot+=calcSingles(grid,shipsizes[1])
shipsizes[shipsize_0] -= 1
for i in range(n):
    for c in range(n-shipsize_0+1):
        if all(grid[i][c:c+shipsize_0]):
            for y in range(c,c+shipsize_0):
                grid[i][y] = 0
            if not any(shipsizes):
                tot+=all([1-grid[o[0]][o[1]] for o in Os])
            shipsize_1 = max([i for i,x in enumerate(shipsizes) if x != 0])
            for y in range(c,c+shipsize_0):
                grid[i][y] = 1
        vert = [grid[c_i][i] for c_i in range(c,c+shipsize_0)]
        if all(vert): 
            for x in range(c,c+shipsize_0):
                grid[x][i] = 0
            tot += solveGrid(grid,shipsizes)
            for x in range(c,c+shipsize_0):
                grid[x][i] = 1
    shipsizes[shipsize_0] += 1





print(solveGrid(grid,shipsizes))
#print(time.time()-totStart)
#print(placementTime)
        
