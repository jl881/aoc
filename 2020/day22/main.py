from time import sleep

deck1history = [[]]
deck2history = [[]]
num_of_games = 0


def starting_decks():
    f = open("input")
    f.readline()
    line = f.readline()
    deck1 = []
    while line:
        deck1.append(int(line))
        line = f.readline().strip()
    f.readline()
    line = f.readline()
    deck2 = []
    while line:
        deck2.append(int(line))
        line = f.readline().strip()
    return deck1, deck2


def calculate_score(deck1, deck2):
    cards = deck1 if len(deck1) > 0 else deck2
    accumulator = 0
    num_of_cards = len(cards)
    for i in range(num_of_cards):
        accumulator += cards[i] * (num_of_cards - i)
    return accumulator


def check_history(deck1, deck2, game_no):
    if deck1 not in deck1history[game_no] and deck2 not in deck2history[game_no]:
        deck1history[game_no].append(deck1[:])
        deck2history[game_no].append(deck2[:])
        return True
    else:
        return False


def play_game(deck1, deck2):
    global num_of_games
    while len(deck1) != 0 and len(deck2) != 0:
        card1, card2 = deck1.pop(0), deck2.pop(0)
        enough1, enough2 = len(deck1) >= card1, len(deck2) >= card2
        if enough1 and enough2:
            num_of_games += 1
            deck1history.append([])
            deck2history.append([])
            print("start game", num_of_games)
            winner = game_recurse(deck1[:card1], deck2[:card2], num_of_games)
            print("back to game 0")
            if winner == 1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        # sleep(1)
    print(deck1, deck2)
    print(calculate_score(deck1, deck2))


def game_recurse(deck1, deck2, game_no):
    global num_of_games
    d1 = deck1[:]
    d2 = deck2[:]
    while len(d1) != 0 and len(d2) != 0:
        print(d1)
        print(d2)
        if check_history(d1, d2, game_no):
            card1, card2 = d1.pop(0), d2.pop(0)
            enough1, enough2 = len(d1) >= card1, len(d2) >= card2
            if enough1 and enough2:
                num_of_games += 1
                deck1history.append([])
                deck2history.append([])
                print("start game", num_of_games)
                winner = game_recurse(d1[:card1], d2[:card2], num_of_games)
                print("back to game", game_no)
                if winner == 1:
                    d1.append(card1)
                    d1.append(card2)
                else:
                    d2.append(card2)
                    d2.append(card1)
            else:
                if card1 > card2:
                    d1.append(card1)
                    d1.append(card2)
                else:
                    d2.append(card2)
                    d2.append(card1)
        else:
            print("winner of game", game_no, ":", 1, "infinite loop")
            return 1
    finalwinner = 1 if len(d1) > 0 else 2
    print("winner of game", game_no, ":", finalwinner)
    return finalwinner


def run_main():
    deck1, deck2 = starting_decks()
    play_game(deck1, deck2)


if __name__ == '__main__':
    run_main()
