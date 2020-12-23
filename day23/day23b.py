from time import sleep
from collections import deque
num_of_cups = 1000000


def do_stuff():
    global num_of_cups
    cup_order = deque(map(int, (list("167248359"))))
    for i in range(len(cup_order) + 1, num_of_cups + 1):
        cup_order.append(i)
    for i in range(10000000):
        if cup_order[0] == 1:
            destination_label = num_of_cups
        else:
            destination_label = cup_order[0] - 1
        while True:
            if destination_label == cup_order[1] or destination_label == cup_order[2] or destination_label == cup_order[3]:
                if destination_label == 1:
                    destination_label = num_of_cups
                else:
                    destination_label = destination_label - 1
            else:
                break
        location = cup_order.index(destination_label)
        this_label = cup_order.popleft()
        for k in range(3):
            cup_order.insert(location, cup_order[0])
            cup_order.popleft()
        cup_order.append(this_label)
    location1 = cup_order.index(1)
    print(cup_order[location1])
    print(cup_order[(location1+1)%num_of_cups])
    print(cup_order[(location1+2)%num_of_cups])



if __name__ == '__main__':
    do_stuff()
