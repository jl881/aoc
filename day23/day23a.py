def do_stuff():
    cup_order = list(map(int, (list("389125467"))))
    num_of_cups = len(cup_order)
    for i in range(100):
        print(cup_order)
        removed_cups = cup_order[1:4]
        cup_truncated = [cup_order[0]] + cup_order[4:]
        this_label = cup_order[0]
        if this_label == 1:
            destination_label = 9
        else:
            destination_label = this_label -1
        search_index = 1
        while True:
            if destination_label in removed_cups:
                if destination_label == 1:
                    destination_label = 9
                else:
                    destination_label = destination_label - 1
            else:
                if destination_label != cup_truncated[search_index]:
                    search_index = (search_index+1)%(num_of_cups-3)
                else:
                    break
        cup_order = cup_truncated[1:search_index+1] + removed_cups + cup_truncated[search_index+1:] + [cup_truncated[0]]
    print(cup_order)



if __name__ == '__main__':
    do_stuff()
