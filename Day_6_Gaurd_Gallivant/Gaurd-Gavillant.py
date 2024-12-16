import sys
from itertools import cycle
from copy import deepcopy
from time import perf_counter

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

# Start moving the guard forward
i_change = -1 # Moving up a 2d array = reduce row number
j_change = 0

# First 90 degree rotation: i = 0, j = 1
# Second 90 degree rotation: i = 1, j = 0
# Third 90 degree rotation: i = 0, j = -1
# Fourth 90 degree rotation: i = -1, j = 0
# Thank these guys https://stackoverflow.com/questions/23416381/circular-list-iterator-in-python
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pool = cycle(directions)

direction = next(pool)
part1 = 0
R = len(grid[0]) # Total rows
C = len(grid[1]) # Total columns

current_pos = guard_position
while (current_pos[0] < R and current_pos[0] >= 0 and current_pos[1] < C and current_pos[1] >= 0):
    #print(current_pos)
    if grid[current_pos[0]][current_pos[1]] == '#':
        current_pos[0] -= direction[0]
        current_pos[1] -= direction[1]
        direction = next(pool)
        continue
    grid[current_pos[0]][current_pos[1]] = 'X'
    if not visited_positions[current_pos[0]][current_pos[1]]:
        part1 += 1
    visited_positions[current_pos[0]][current_pos[1]] = True
    current_pos[0] += direction[0]
    current_pos[1] += direction[1]

for row in grid:
    print(''.join(row))
print(part1)
