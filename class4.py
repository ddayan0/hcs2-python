#class4.py
#Dennis Dayan
import random



def line():
    print('-----------------------------------\n')

class Card:

    cardsuitlist = ['hearts', 'diamonds', 'clubs', 'spades',]
    cardfacelist = [2, 3, 4, 5, 6, 7 , 8, 9, 10, 'ace', 'jack', 'queen', 'king']
    def __init__(self):
       self.suit = Card.cardsuitlist[random.randint(0, 3)]
       self.face = Card.cardfacelist[random.randint(0, len(Card.cardfacelist)-1)]
       self.value = Card.value_calc(self)
    def value_calc(self):
        if type(self.face) == int:
            return(self.face)
        if self.face == 'ace':
            return(11)
        if self.face == 'jack':
            return(11)
        if self.face == 'queen':
            return(12)
        if self.face == 'king':
            return(13)

class Hand:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.value = Hand.cardcalc(self)
    def cardcalc (self):
        return(self.card1.value + self.card2.value)

card1 = Card()
card2 = Card()
card3 = Card()
card4 = Card()
myhand = Hand(card1, card2)
comphand = Hand(card3, card4)


def play():
    running = True
    while running:
        print('WELCOME TO THE GREATEST CARD GAME IN THE HISTORY OF CARD GAMES')
        print('WOULD YOU LIKE TO PLAY?')
        usinput = str(input('Y/N?'))
        if usinput == 'N' or 'n':
            import sys
            sys.exit(0)
        if usinput == 'Y' or 'y':
            print('MY CARDS ARE {} and {} WHICH TOTAL TO {}'.format(card1.face, card2.face, myhand.value)) #computers hand
            if comphand.value > 21:
                print('I LOSE, YOU WIN')
            if comphand.value < 21:
                print('YOUR TURN')
                print('YOUR CARDS ARE {} and {} WHICH TOTAL TO {}'.format(card3.face, card4.face, comphand.value))#user hand
                if myhand.value > 21:
                    print('ITS A DRAW!!')
                if myhand.value < 21:
                    print('ITS A DRAW!')
                else:
                    print('NOOOOOO YOU WINNNNNNNNNNNNN!')

            else:
                print('I WINNNNNN!!!!!!!')
                import sys
                sys.exit(0)

play()


