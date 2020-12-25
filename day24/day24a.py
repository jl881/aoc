def get_coord(line):
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


def run_main():
    black = []

    f = open("testinput")
    line = f.readline().strip()
    while line:
        coord = get_coord(line)
        print(coord)
        if coord in black:
            black.remove(coord)
        else:
            black.append(coord)
        line = f.readline().strip()
    print(len(black))


if __name__ == '__main__':
    run_main()
