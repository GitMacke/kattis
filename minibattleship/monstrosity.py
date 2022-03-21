
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
n_ones = shipsizes[1]
def calcSingles(grid):
    nsingles = n_ones
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
shipsize_zero = max([i for i,x in enumerate(shipsizes) if x != 0],default = 0)
shipsizes[shipsize_zero] -= 1
shipsize_one = max([i for i,x in enumerate(shipsizes) if x != 0], default = 0)
shipsizes[shipsize_one] -= 1
shipsize_two = max([i for i,x in enumerate(shipsizes) if x != 0],default = 0)
shipsizes[shipsize_two] -= 1
shipsize_three = max([i for i,x in enumerate(shipsizes) if x != 0], default = 0)
shipsizes[shipsize_three] -= 1
shipsize_four = max([i for i,x in enumerate(shipsizes) if x != 0], default = 0)
shipsizes[shipsize_four] -= 1
shipsizes[0] = 0



if shipsize_zero == 0:
    tot += all([1-grid[o[0]][o[1]] for o in Os])
elif shipsize_zero == 1:
    tot += calcSingles(grid)
else:
    for i_zero in range(n):
        for c_zero in range(n-shipsize_zero+1):
            if all(grid[i_zero][c_zero:c_zero+shipsize_zero]):
                for y in range(c_zero,c_zero+shipsize_zero):
                    grid[i_zero][y] = 0
                #FROM HERE
                if shipsize_one == 0:
                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                elif shipsize_one == 1:
                    tot+=calcSingles(grid)
                else:
                    for i_one in range(n):
                        for c_one in range(n-shipsize_one+1):
                            if all(grid[i_one][c_one:c_one+shipsize_one]):
                                for y in range(c_one,c_one+shipsize_one):
                                    grid[i_one][y] = 0
                                #FROM HERE
                                if shipsize_two == 0:
                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                elif shipsize_two == 1:
                                    tot+=calcSingles(grid)
                                else:
                                    for i_two in range(n):
                                        for c_two in range(n-shipsize_two+1):
                                            if all(grid[i_two][c_two:c_two+shipsize_two]):
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERE
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 1
                                            vert = [grid[c_i][i_two] for c_i in range(c_two,c_two+shipsize_two)]
                                            if all(vert): 
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERRE
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 1
                                #TO HERE
                                for y in range(c_one,c_one+shipsize_one):
                                    grid[i_one][y] = 1
                            vert = [grid[c_i][i_one] for c_i in range(c_one,c_one+shipsize_one)]
                            if all(vert): 
                                for x in range(c_one,c_one+shipsize_one):
                                    grid[x][i_one] = 0
                                #FROM HERE
                                if shipsize_two == 0:
                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                elif shipsize_two == 1:
                                    tot+=calcSingles(grid)
                                else:
                                    for i_two in range(n):
                                        for c_two in range(n-shipsize_two+1):
                                            if all(grid[i_two][c_two:c_two+shipsize_two]):
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERE
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 1
                                            vert = [grid[c_i][i_two] for c_i in range(c_two,c_two+shipsize_two)]
                                            if all(vert): 
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERRE
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 1
                                #TO HERRE
                                for x in range(c_one,c_one+shipsize_one):
                                    grid[x][i_one] = 1
                #TO HERE
                for y in range(c_zero,c_zero+shipsize_zero):
                    grid[i_zero][y] = 1
            vert = [grid[c_i][i_zero] for c_i in range(c_zero,c_zero+shipsize_zero)]
            if all(vert): 
                for x in range(c_zero,c_zero+shipsize_zero):
                    grid[x][i_zero] = 0
                #FROM HERE
                if shipsize_one == 0:
                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                elif shipsize_one == 1:
                    tot+=calcSingles(grid)
                else:
                    for i_one in range(n):
                        for c_one in range(n-shipsize_one+1):
                            if all(grid[i_one][c_one:c_one+shipsize_one]):
                                for y in range(c_one,c_one+shipsize_one):
                                    grid[i_one][y] = 0
                                #FROM HERE
                                if shipsize_two == 0:
                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                elif shipsize_two == 1:
                                    tot+=calcSingles(grid)
                                else:
                                    for i_two in range(n):
                                        for c_two in range(n-shipsize_two+1):
                                            if all(grid[i_two][c_two:c_two+shipsize_two]):
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERE
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 1
                                            vert = [grid[c_i][i_two] for c_i in range(c_two,c_two+shipsize_two)]
                                            if all(vert): 
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERRE
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 1
                                #TO HERE
                                for y in range(c_one,c_one+shipsize_one):
                                    grid[i_one][y] = 1
                            vert = [grid[c_i][i_one] for c_i in range(c_one,c_one+shipsize_one)]
                            if all(vert): 
                                for x in range(c_one,c_one+shipsize_one):
                                    grid[x][i_one] = 0
                                #FROM HERE
                                if shipsize_two == 0:
                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                elif shipsize_two == 1:
                                    tot+=calcSingles(grid)
                                else:
                                    for i_two in range(n):
                                        for c_two in range(n-shipsize_two+1):
                                            if all(grid[i_two][c_two:c_two+shipsize_two]):
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERRE
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])#SOLVE HERE
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERE
                                                for y in range(c_two,c_two+shipsize_two):
                                                    grid[i_two][y] = 1
                                            vert = [grid[c_i][i_two] for c_i in range(c_two,c_two+shipsize_two)]
                                            if all(vert): 
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 0
                                                #FROM HERE
                                                if shipsize_three == 0:
                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                elif shipsize_three == 1:
                                                    tot+=calcSingles(grid)
                                                else:
                                                    for i_three in range(n):
                                                        for c_three in range(n-shipsize_three+1):
                                                            if all(grid[i_three][c_three:c_three+shipsize_three]):
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERE
                                                                for y in range(c_three,c_three+shipsize_three):
                                                                    grid[i_three][y] = 1
                                                            vert = [grid[c_i][i_three] for c_i in range(c_three,c_three+shipsize_three)]
                                                            if all(vert): 
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 0
                                                                #FROM HERE
                                                                if shipsize_four == 0:
                                                                    tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                elif shipsize_four == 1:
                                                                    tot+=calcSingles(grid)
                                                                else:
                                                                    for i_four in range(n):
                                                                        for c_four in range(n-shipsize_four+1):
                                                                            if all(grid[i_four][c_four:c_four+shipsize_four]):
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                                #TO HERE
                                                                                for y in range(c_four,c_four+shipsize_four):
                                                                                    grid[i_four][y] = 1
                                                                            vert = [grid[c_i][i_four] for c_i in range(c_four,c_four+shipsize_four)]
                                                                            if all(vert): 
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 0
                                                                                #FROM HERE
                                                                                tot += all([1-grid[o[0]][o[1]] for o in Os])
                                                                                #TO HERRE
                                                                                for x in range(c_four,c_four+shipsize_four):
                                                                                    grid[x][i_four] = 1
                                                                #TO HERRE
                                                                for x in range(c_three,c_three+shipsize_three):
                                                                    grid[x][i_three] = 1
                                                #TO HERRE
                                                for x in range(c_two,c_two+shipsize_two):
                                                    grid[x][i_two] = 1
                                #TO HERRE
                                for x in range(c_one,c_one+shipsize_one):
                                    grid[x][i_one] = 1
                #TO HERE
                for x in range(c_zero,c_zero+shipsize_zero):
                    grid[x][i_zero] = 1

print(tot)

        
