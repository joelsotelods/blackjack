'''
BlackJack

Version: Computer Dealer and 1 Human Player.

Computer Dealer

Deck 52 cards
Player


The player has a bank roll

The player can put a bet.


The player starts with two cards face up
the computer dealer starts with 1 card face up and a card face down

The player goal is to get closer to a total value of 21 than the dealer does.

The current value is the sum of the two cards the player has.

Possible actions:
    Hit:
        Receive another card from the deck

    Stay:
        Stop Receiving Cards

Hit receive a new card face up.

If the player is still under 21.. the dealer hast to hit until:
1) he beats the player
2) busts (go over 21)

the game ends when:

1) if the player busts before the computer.. he losts and he loses the bet
    the dealer collects the money

2)
Rules:
Jack, Queen, King count as 10
Aces can count as either 1 or 11 depending on the player preference.




'''

from random import randint

class Deck:

    def __init__(self, pswhat):
        self.cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', \
                    'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',\
                    'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', \
                    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',\
                    'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', \
                    'Nine', 'Ten', 'Jack', 'Queen', 'King',\
                    'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', \
                    'Ten', 'Jack', 'Queen', 'King']

        self.playernum = pswhat

    def numberofcards(self):
        return len(self.cards)

    def getdeck(self):
        return self.cards

    def shufflecards(self):

        cards_tmp = []

        rand = -1

        while ( len(self.cards) > 0):

            rand = randint(0, len(self.cards)-1)
            cards_tmp.append(self.cards[rand])
            del self.cards[rand]

        self.cards = cards_tmp

    def emptydeck(self):
        self.cards = []


class Wallet:

    def __init__(self, initialamount):

        self.balance = initialamount

    def retire(self, amount):

        self.balance = self.balance - amount

    def add(self, amount):

        self.balance = self.balance + amount
    

def playahand(maindeck, playerinturn):

    player = playerinturn

    cardvalues = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}
    
    # player
    if (player.playernum == 1):

        print('The You have: ')
        playerdeck = player.getdeck()
        print(playerdeck)

        playerscore = getscore(playerdeck,cardvalues)

        print('Your current score is {}'.format(playerscore))

        while (input('Do you wanna Hit?: ') == 'Yes'):

            newcard = maindeck.cards.pop()
            player.cards.append(newcard)

            playerdeck = player.getdeck()
            print(playerdeck)

            playerscore = getscore(playerdeck,cardvalues)

            if playerdeck[-1] == 'Ace':
                if input('Do you wanna use your Ace as 1 or as 11?') == '11':
                    playerscore = playerscore + 10

            print('Your current score is {}'.format(playerscore))
            
            if playerscore > 21:
                break
    
    #Dealer
    if (player.playernum == 2):
        
        print('The Dealer has: ')
        playerdeck = player.getdeck()
        print(playerdeck)

        playerscore = getscore(playerdeck,cardvalues)

        print('The Dealer s current score is {}'.format(playerscore))
        
        while (playerscore < 17):
            input('Dealer will get another card.. press enter')

            newcard = maindeck.cards.pop()
            player.cards.append(newcard)

            playerdeck = player.getdeck()
            print(playerdeck)

            playerscore = getscore(playerdeck,cardvalues)

            print('The Dealer s current score is {}'.format(playerscore))
            
            if playerscore > 21:
                break

            print('The Dealer has: ')
            playerdeck = player.getdeck()
            print(playerdeck)

            print('The Dealer s current score is {}'.format(playerscore))




    return playerscore



def getscore(list, cval):

    score = 0

    for n in list:
        score = cval[n] + score

    return score





def playgame():


    maindeck = Deck(0)
    maindeck.shufflecards()

    player = Deck(1)
    player.emptydeck()

    dealer = Deck(2)
    dealer.emptydeck()

    # player takes card
    newcard = maindeck.cards.pop()
    player.cards.append(newcard)

    if player.cards[-1] == 'Ace':
        if input('Do you wanna use your Ace as 1 or as 11?') == '11':
            playerscore = playerscore + 10

    # Dealer takes card
    newcard = maindeck.cards.pop()
    dealer.cards.append(newcard)

    # Player takes card
    newcard = maindeck.cards.pop()
    player.cards.append(newcard)

    # Dealer takes card
    newcard = maindeck.cards.pop()
    dealer.cards.append(newcard)

    print('The Dealer has {} and another card faced down'.format(dealer.cards[0]))

    playerscore = playahand(maindeck,player)

    if playerscore < 22:
        dealerscore = playahand(maindeck,dealer)
    else:
        return False


    if dealerscore > 21:
        return True
    elif dealerscore < playerscore:
        return True
    else:
        return False


def main():
    playerwallet = Wallet(5000)

    print('You have {}. '.format(playerwallet.balance))

    while True:
        bet = int(input('How much do you wanna bet?: '))

        if playgame():
            print('You Won {}'.format(bet*2))
            playerwallet.add(bet)
        else:
            print('You Lost {}'.format(bet))
            playerwallet.retire(bet)

        print('your current balance is {}'.format(playerwallet.balance))

        if (input('Do you wanna play again?') != 'Yes'):
            print('bye')
            break

main()

'''
# 1=Hearts 2=Diamonds 3=Spades 4=Clubs 
all_cards = {1:cards, 2:cards, 3:cards, 4:cards}


print(all_cards)

money = int(input('How much money do you have?'))

bettingmoney = int(input('How much money do you wanna bet?'))

if bettingmoney <money:
'''