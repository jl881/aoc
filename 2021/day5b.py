import numpy as np

grid = np.zeros((1000, 1000), np.int8)


def populate():
    f = open("input/day5a.txt")
    lines = f.readlines()
    for line in lines:
        line_split = line.strip().split(" -> ")
        coord1 = tuple(map(int, line_split[0].split(",")))
        coord2 = tuple(map(int, line_split[1].split(",")))
        if coord1[0] == coord2[0]:  # horizontal
            bigger_col = coord1[1] if coord1[1] > coord2[1] else coord2[1]
            smaller_col = coord1[1] if coord1[1] < coord2[1] else coord2[1]
            row = coord1[0]
            grid[row, smaller_col:bigger_col+1] += 1
        elif coord1[1] == coord2[1]:  # vertical
            bigger_row = coord1[0] if coord1[0] > coord2[0] else coord2[0]
            smaller_row = coord1[0] if coord1[0] < coord2[0] else coord2[0]
            col = coord1[1]
            grid[smaller_row:bigger_row+1, col] += 1
        else:
            # two diagonal cases
            x1, y1 = coord1 if coord1[0] < coord2[0] else coord2
            x2, y2 = coord1 if coord1[0] > coord2[0] else coord2
            steps = x2 - x1 + 1
            if (y2 - y1) == (x2 - x1):
                for i in range(steps):  # slanting right
                    grid[x1 + i, y1 + i] += 1
            elif (y1 - y2) == (x2 - x1):  # slanting left
                for i in range(steps):
                    grid[x1 + i, y1 - i] += 1


def run_main():
    populate()
    print(np.count_nonzero(grid >= 2))


if __name__ == '__main__':
    run_main()
