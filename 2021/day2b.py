def run_main():
    horizontal = 0
    depth = 0
    aim = 0
    f = open("input/day2a.txt")
    line = f.readline()
    while line:
        split_instruction = line.strip().split(" ")
        direction = split_instruction[0]
        number = int(split_instruction[1])
        if direction == "forward":
            horizontal += number
            depth += aim * number
        elif direction == "up":
            aim -= number
        elif direction == "down":
            aim += number
        line = f.readline()
    print("horizontal", horizontal)
    print("depth", depth)
    print("product", horizontal * depth)


if __name__ == '__main__':
    run_main()
