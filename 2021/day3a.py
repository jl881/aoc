def run_main():
    f = open("input/day3a.txt")
    lines = f.readlines()
    listify = lambda line: list(map(int, list(line.strip())))
    grid = list(map(listify, lines))
    gamma_no = gamma(grid)
    epsilon_no = epsilon(grid)
    gamma_dec = int(gamma_no, 2)
    epsilon_dec = int(epsilon_no, 2)
    print(gamma_dec * epsilon_dec)


def gamma(grid):
    gamma_string = ""
    for i in range(0, 12):
        sum_of_column = 0
        for row in grid:
            sum_of_column += row[i]
        if sum_of_column > 500:
            gamma_string = gamma_string + "1"
        else:
            gamma_string = gamma_string + "0"
    return gamma_string


def epsilon(grid):
    epsilon_string = ""
    for i in range(0, 12):
        sum_of_column = 0
        for row in grid:
            sum_of_column += row[i]
        if sum_of_column > 500:
            epsilon_string = epsilon_string + "0"
        else:
            epsilon_string = epsilon_string + "1"
    return epsilon_string


if __name__ == '__main__':
    run_main()
