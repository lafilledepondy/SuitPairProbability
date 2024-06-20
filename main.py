import random

deck_of_cards = ['1 ♤', '2 ♤', '3 ♤',  '4 ♤', '5 ♤', 
                 '6 ♤', '7 ♤', '8 ♤', '9 ♤', '10 ♤', 
                 '11 ♤', '12 ♤', '13 ♤', 

                 '1 ◆', '2 ◆', '3 ◆',  '4 ◆', '5 ◆', 
                 '6 ◆', '7 ◆', '8 ◆', '9 ◆', '10 ◆', 
                 '11 ◆', '12 ◆', '13 ◆', 

                 '1 ❤' '2 ❤', '3 ❤',  '4 ❤', '5 ❤', 
                 '6 ❤', '7 ❤', '8 ❤', '9 ❤', '10 ❤', 
                 '11 ❤', '12 ❤', '13 ❤', 

                 '1 ♧', '2 ♧', '3 ♧',  '4 ♧', '5 ♧', 
                 '6 ♧', '7 ♧', '8 ♧', '9 ♧', '10 ♧', 
                 '11 ♧', '12 ♧', '13 ♧']


def shuffled(cards):
    random.shuffle(cards)

def size (cards):
    return len(cards)

def display(cards):
    print(*cards, sep = "  ; ")

def conscePairs(cards):
    res = []

    for i in range(size(cards) - 1):
        card1 = cards[i].split()
        card2 = cards[i + 1].split()

        rank1 = int(card1[0])
        rank2 = int(card2[0])

        if (rank2 == rank1 + 1 and card1[1] == card2[1]):
            res.append([cards[i], cards[i + 1]])

    return res

def main():
    print("A standard deck of 52 cards: ")
    display(deck_of_cards)
    
    print("\n" + "Shuffled deck: ")
    shuffled(deck_of_cards)
    display(deck_of_cards)

    res = conscePairs(deck_of_cards)
    print("\n" + "There are " + str(size(res)) + " sequence of 2 of the same suit.")
    print(res)
    
    return 

if __name__ == "__main__":
    main()