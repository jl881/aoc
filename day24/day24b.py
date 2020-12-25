import numpy as np

def parse_coord(line):
    half = False
    x, y = 0, 0
    for pos in range(len(line)):
        current_char = line[pos]
        if not half:
            if current_char == "e":
                x += 2
            elif current_char == "w":
                x -= 2
            elif current_char == "s":
                y -= 2
                half = True
            elif current_char == "n":
                y += 2
                half = True
        else:
            if current_char == "e":
                x += 1
            elif current_char == "w":
                x -= 1
            half = False
    return (x, y)

def get_indices(coord):
    return (coord[0]+200, coord[1]+200)


def initialise():
    grid = np.zeros((400,400))

    f = open("input")
    line = f.readline().strip()
    while line:
        coord = parse_coord(line)
        indices = get_indices(coord)
        grid[indices] = 1 if grid[indices] == 0 else 0
        line = f.readline().strip()
    return grid

def play(grid):
    neighbours = [(1, 2), (2, 0), (1, -2), (-1, -2), (-2, 0), (-1, 2)]
    neighbour_vectors = list(map(np.array, neighbours))

    grid_copy = np.copy(grid)
    for y in range(-198, 198, 2):
        start = -198 if y%4 == 0 else -197

        end = 198 if y%4 == 0 else 199

        for x in range(start,end, 2):
            location = np.array(get_indices((x, y)))
            addloc = lambda vec : vec + location
            neighbour_locations = map(addloc, neighbour_vectors)
            getval = lambda vec: grid[tuple(vec)]
            neighbour_values = map(getval, neighbour_locations)
            num_of_blacks = sum(neighbour_values)
            this_tile = grid[tuple(location)]
            if this_tile == 0:
                if num_of_blacks == 2:
                    grid_copy[tuple(location)] = 1
            elif this_tile == 1:
                if num_of_blacks == 0 or num_of_blacks > 2:
                    grid_copy[tuple(location)] = 0

    return grid_copy


def run_main():
    grid = initialise()

    for i in range(100):
        grid = play(grid)
        print(i, np.sum(grid))
if __name__ == '__main__':
    run_main()
