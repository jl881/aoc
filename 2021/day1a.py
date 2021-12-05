def run_main():
    increases = 0
    old_no = -1
    f = open("input/day1a.txt")
    line = f.readline()
    while line:
        current_no = int(line.strip())
        if -1 < old_no < current_no:
            increases += 1
        old_no = current_no
        line = f.readline()
    print(increases)


if __name__ == '__main__':
    run_main()
