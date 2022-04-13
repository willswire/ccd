# Refer to README.md for the problem instructions


def findGutsWinner(hand1, hand2):
    # check to see if either hand is improper
    if (improperHand(hand1) or improperHand(hand2)):
        return []     
    # if the first hand is three of a kind
    elif threeOfAKind(hand1):
        if threeOfAKind(hand2):
            if hand1[0] > hand2[0]:
                return hand1
            else:
                return hand2
        else:
            return hand1
    # if the second hand is three of a kind
    elif threeOfAKind(hand2):
        if threeOfAKind(hand1):
            if hand1[0] > hand2[0]:
                return hand1
            else:
                return hand2
        else:
            return hand2
    # if the first hand is two of a kind
    elif twoOfAKind(hand1):
        if twoOfAKind(hand2):
            if twoOfAKind(hand1) > twoOfAKind(hand2):
                return hand1
            else:
                return hand2
        else:
            return hand1
    # if the second hand is two of a kind
    elif twoOfAKind(hand2):
        if twoOfAKind(hand1):
            if twoOfAKind(hand1) > twoOfAKind(hand2):
                return hand1
            else:
                return hand2
        else:
            return hand2
    # if either hand has a high card
    else:
        return highCard(hand1, hand2)

def improperHand(hand):
    return len(hand) != 3 

def threeOfAKind(hand):
    if(hand[0] == hand[1] == hand[2]):
        return hand[0]
    else:
        return 0

def twoOfAKind(hand):
    if hand.count(hand[0]) == 2:
        return hand[0]
    elif hand.count(hand[1]) == 2:
        return hand[1]
    else:
        return 0

def highCard(hand1, hand2):
    if(max(hand1) > max(hand2)):
        return hand1
    else:
        return hand2
