import numpy as np
num_of_boards = 100
boards = np.zeros((num_of_boards, 5, 5), np.int8)


def initialise():
    f = open("input/day4a.txt")
    global calling_order
    calling_order = list(map(int, f.readline().strip().split(",")))
    f.readline()
    line = f.readline()
    for board in range(0, num_of_boards):
        for row_no in range(0, 5):
            row = list(map(int, line.strip().split()))
            boards[board][row_no] = np.array(row)
            line = f.readline()
        line = f.readline()


def find_last_winning():
    not_winning = []
    for board in boards:
        this_winning = False
        for row in board:
            if all(element == -1 for element in row):
                this_winning = True
                break
        if not this_winning:
            for col in range(0, 5):
                if all(row[col] == -1 for row in board):
                    this_winning = True
                    break
        if not this_winning:
            not_winning.append(board)
    if len(not_winning) == 1:
        return not_winning[0]


def find_winning():
    for board in boards:
        for row in board:
            if all(element == -1 for element in row):
                return board
        for col in range(0, 5):
            if all(row[col] == -1 for row in board):
                return board


def play_bingo():
    global called
    called = calling_order.pop(0)
    boards[boards == called] = -1


def run_main():
    global boards
    initialise()
    last_winning = None
    while last_winning is None:
        play_bingo()
        last_winning = find_last_winning()
    boards = np.zeros((1, 5, 5), np.int8)
    boards[0] = last_winning

    winning = None
    while winning is None:
        play_bingo()
        winning = find_winning()
    add_remaining = np.sum(winning, where=winning > -1)
    print(add_remaining * called)


if __name__ == '__main__':
    run_main()
