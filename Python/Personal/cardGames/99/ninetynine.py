import Player as p
import random
        

def create_deck(num_d):
    suit = ['H', 'D', 'C', 'S']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []

    for i in range(num_d): 
        for s in suit:
            for v in values:
                deck.append(v + s)
    return deck


def get_cards(deck):
    return deck[:5]



def card_score(card):
    plain_points = ['2', '3', '5', '6', '7', '8', 'J', 'Q']
    no_points = [4, 9, 10]

    if len(card) == 3:
        c = card[:2]
    else:
        c = card[0]

    if c in plain_points:
        if c.isdigit():
            return int(c)
        else:
            return 10
    elif c == 'K':
        return 99
    elif int(c) in no_points:
        if int(c) == 4:
            return -4
        if int(c) == 10:
            return -10
        else:
            return 0
    elif int(c) == 1:
        choice = True
        while choice:
            choice = int(input("Would you like to add: \n\t1. 1 point\n\t2. 11 points"))
            if choice == 1:
                return 1
            elif choice == 2:
                return 11
            else:
                print("Invalid Input")
                continue
    


def play(player, d):
    p = player
    card = p.play_card()
    x = card_score(card)
    p.draw(d)
    del d[0]
    if x == -4:
        return [0, -1]
    else:
        return [x, 0]


def main():
        deck = []
        num_p = int(input("How many players are playing: "))
        if num_p == 2:
            deck = create_deck(1)
        elif 2 < num_p < 5:
            deck = create_deck(2)
        else:
            deck = create_deck(3)
        random.shuffle(deck)

        players = []
        for i in range(num_p):
            x = get_cards(deck)
            players.append(p.Player(x, i + 1))
            del deck[:5]
        
        play_direction = 1
        pile_total = 0
        turn = 0
        while pile_total <= 99:
            for player in range(len(players)):
                if turn == 0:
                    score = play(players[player], deck)
                else:
                    score = play(players[player + (play_direction * 2)], deck)
                if score[0] == 99:
                    pile_total = 99
                else:
                    if (pile_total + score[0]) < 0:
                        pile_total = 0
                    else:
                        pile_total += score[0]
                play_direction = score[1]
                turn += 1
                
                print("Pile value: " + str(pile_total))
                if pile_total > 99:
                    print("Player {} lost!".format(players[player].get_pnum()))
                    break
    

if __name__ == '__main__':
    main()
    
    
