import sys
from itertools import cycle
from copy import deepcopy

filename = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"

with open(filename, mode='r') as file:
    grid = [list(i.replace('\n', '')) for i in file.readlines()]
visited_positions = [[False,]*len(grid[0]) for i in grid]
# print(visited_positions)

# Get the position of the guard, I'm just gonna assume she starts moving forward, i.e, upwards in relation to the graph

guard_position = [0,0]
guard_char = "^"

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == guard_char:
            guard_position[0] = i
            guard_position[1] = j
            break


# First 90 degree rotation: i = 0, j = 1
# Second 90 degree rotation: i = 1, j = 0
# Third 90 degree rotation: i = 0, j = -1
# Fourth 90 degree rotation: i = -1, j = 0
# Thank these guys https://stackoverflow.com/questions/23416381/circular-list-iterator-in-python
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pool = cycle(directions)

part2 = 0
R = len(grid[0]) # Total rows
C = len(grid[1]) # Total columns

def printgrid(grid):
    for row in grid:
        print(''.join(row))

print("Original Grid: ")
printgrid(grid)
print("_"*10)

for i in range(R):
    print(i)
    for j in range(C):
        #print("New Graph Combination")
        new_grid = deepcopy(grid)
        dirchange = 0
        direction = directions[dirchange % 4]
        current_pos = deepcopy(guard_position)
        if new_grid[i][j] == '^' or new_grid[i][j] == '#':
            continue

        new_grid[i][j] = '#'
        #print(f'Obstacle at {i},{j}')
        #printgrid(new_grid)
        visited = set() # Sets of (r, c, d, state)
        while (current_pos[0] < R and current_pos[0] >= 0 and current_pos[1] < C and current_pos[1] >= 0):
            #print("Iterating")
            #print(direction)
            state = False
            #if ((current_pos[0], current_pos[1], direction, state)) in visited:
            #    print(f"{visited}:{(current_pos[0], current_pos[1], direction, False)}: infinite detected")
            #    part2 += 1
            #    break #print(current_pos)
            if new_grid[current_pos[0]][current_pos[1]] == '#':
                current_pos[0] -= direction[0]
                current_pos[1] -= direction[1]
                dirchange += 1
                direction = directions[dirchange % 4]
                #print(f"Direction changed to {direction}")
                state = True
                if (current_pos[0], current_pos[1], direction, state) in visited:
                    #print("Infinite")
                    part2 += 1
                    direction = direction[0]
                    break
                else:
                    #print(f"Added visit point at point before obstacle {current_pos[0]}, {current_pos[1]}")
                    visited.add((current_pos[0], current_pos[1], direction, state))
            else:
                #new_grid[current_pos[0]][current_pos[1]] = 'X'
                visited.add((current_pos[0], current_pos[1], direction, state))
                #print(f"Added visit point with no collision{current_pos[0]}, {current_pos[1]}")
                # print(f"{visited}:{(current_pos[0], current_pos[1], direction, False)}: Not infinite")
                current_pos[0] += direction[0]
                current_pos[1] += direction[1]
                #printgrid(new_grid)
                #print(visited)
                #print("")
print("______ANSWER________")
print(part2)

