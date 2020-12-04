import ninetynine as nn

class Player:

    def __init__(self, hand, p_num):
        self.hand = hand
        self.p_num = p_num

    def play_card(self):
        x = ''
        keep_going = True

        while keep_going:
            print("Player {}: what would you like to play: ".format(self.p_num))
            print("\t1. {}\n\t2. {}\n\t3. {}\n\t4. {}\n\t5. {}".format(self.hand[0], self.hand[1], self.hand[2], self.hand[3], self.hand[4]))
            opt = int(input())

            if opt <= len(self.hand):
                x = self.hand.pop(opt - 1)
                return x
            else:
                print("Invalid Input")
                continue
                
        print("New Hand: " + str(self.hand))
        return x
        
    
    def get_hand(self):
        for i in self.hand:
            print(i, end=" ")
        print("\n")

    
    def draw(self, deck):
        self.hand.append(deck[0])

    
    def get_pnum(self):
        return self.p_num


if __name__ == '__main__':
    nn.main()