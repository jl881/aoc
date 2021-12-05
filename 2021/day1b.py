def run_main():
    increases = 0
    old_no = -1
    f = open("input/day1a.txt")
    lines = list(map(int, f.readlines()))
    for i in range(0, 1998):
        a = lines[i]
        b = lines[i+1]
        c = lines[i+2]
        current_no = a + b + c
        if -1 < old_no < current_no:
            increases += 1
        old_no = current_no
    print(increases)


if __name__ == '__main__':
    run_main()
