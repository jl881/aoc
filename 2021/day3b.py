def run_main():
    f = open("input/day3a.txt")
    lines = f.readlines()
    listify = lambda line: list(map(int, list(line.strip())))
    grid = list(map(listify, lines))
    oxygen_string = "".join(map(str, oxygen(grid.copy())))
    oxygen_dec = int(oxygen_string, 2)
    co2_string = "".join(map(str, co2(grid.copy())))
    co2_dec = int(co2_string, 2)
    print(oxygen_dec * co2_dec)


def oxygen(grid):
    for column in range(0, 12):
        sum_of_column = 0
        if len(grid) == 1:
            break
        for row in grid:
            sum_of_column += row[column]
        if sum_of_column >= len(grid)/2:
            to_remove = 0
        else:
            to_remove = 1
        grid = remove_num(column, to_remove, grid)
    return grid[0]


def co2(grid):
    for column in range(0, 12):
        sum_of_column = 0
        if len(grid) == 1:
            break
        for row in grid:
            sum_of_column += row[column]
        if sum_of_column >= len(grid)/2:
            to_remove = 1
        else:
            to_remove = 0
        grid = remove_num(column, to_remove, grid)
    return grid[0]


def remove_num(column, to_remove, grid):
    current_index = 0
    while current_index < len(grid):
        row = grid[current_index]
        if row[column] == to_remove:
            del grid[current_index]
        else:
            current_index += 1
    return grid


if __name__ == '__main__':
    run_main()
