import random

class Poker_Agent:

    # identify if there is one or more pairs in the hand

    # Rank: {2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A}
    # Suit: {s, h, d, c}

    # 2 example poker hands
    def __init__(self, money):
      
        self.money = money
        self.dictionary = {}
        self.hand_strength = 0
        i = 2
        for x in "2 3 4 5 6 7 8 9 T J Q K A".split():
            self.dictionary[x] = i
            i += 1
        
    def assignCards(self,CurrentHand):
        self.CurrentHand=CurrentHand      

    def calculateHandStrength(self,name):
        cards = self.CurrentHand
        dic = self.dictionary
        numbers = []
        for x in cards:
            numbers.append(dic[x[0]])
        numbers.sort()


        if name == 'Three of a kind':
    
            self.hand_strength+=50
            self.hand_strength+=numbers[2]
            print numbers

        elif name == 'pair':
            self.hand_strength+=30
            self.hand_strength+=numbers[2]
            print numbers

        elif name == 'HighCard':
            self.hand_strength+=10
            self.hand_strength+=numbers[2]
            print numbers

            
            
    def getHandStrength(self):
        return self.hand_strength
                           
    def getHandofCards(self):
        return self.CurrentHand

    def addMoney(self,winpot):
        self.money += winpot
        #print "Current pot: ", winpot

    def reset_hand_strength(self):
        self.hand_strength = 0
    
    def currentMoney(self):

        print "Current pot: ", self.money

    def Random_Agent(self,phase):    

        self.analyseHand()
        
        if phase == 1:
            bet = random.randrange(1,50,1)
            self.money-=bet
            return bet
        elif phase == 2:
            bet = random.randrange(1,50,1)
            self.money-=bet
            return bet
        elif phase == 3:
            bet = random.randrange(1,50,1)
            self.money-=bet
            
            return bet

    def Reflex_Agent(self,phase):

        self.analyseHand()
        hs = self.hand_strength
        
        if phase == 1:

            if(hs>=10 and hs<30):
                bet = 10
                self.money-=bet
                return bet
            elif(hs>=30 and hs<50):
                bet = 10
                self.money-=bet
                return bet
            elif(hs>=50):
                bet = 10
                self.money-=bet
                return bet

        if phase == 2:

            if(hs>=10 and hs<30):
                bet = 5
                self.money-=bet
                return bet
            elif(hs>=30 and hs<50):
                bet = 10
                self.money-=bet
                return bet
            elif(hs>=50):
                bet = 20
                self.money-=bet
                return bet

        if phase == 3:

            if(hs>=10 and hs<30):
                bet = 5
                self.money-=bet
                return bet
            elif(hs>=30 and hs<50):
                bet = 10
                self.money-=bet
                return bet
            elif(hs>=50):
                bet = 30
                self.money-=bet
                return bet
    


    def Fixed_Agent(self,phase):    

        if phase == 1:
            return 10
        elif phase == 2:
            return 20
        elif phase == 3:
            return 30
        

    # identify hand category using IF-THEN rule
    def identifyHand(self,Hand_):
        for c1 in Hand_:
            for c2 in Hand_:
                if (c1[0] == c2[0]) and (c1[1] < c2[1]):
                    for c3 in Hand_:
                        if (c2[0] == c3[0]) and (c2[1] < c3[1]):
                            return  "Three of a kind"
                            #yield dict(name='Three of a kind',rank=c2[0],suit1=c1[1],suit2=c2[1],suit3=c3[1])
                        elif (c2[0]!= c3[0]):
                            return "pair"
                            #yield dict(name='pair',rank=c1[0],suit1=c1[1],suit2=c2[1], suit3=c3[1])
        return "HighCard"

    # Print out the result
    def analyseHand(self):
        #HandCategory = []

        name = self.identifyHand(self.CurrentHand)
        print name
        self.calculateHandStrength(name)
        #functionToUse = identifyHand
        

#        for category in functionToUse(Hand_):
#            print('Category: ')
#            for key in "name rank suit1 suit2 suit3".split():
                #calculateHandStrength(category[key])
                

class PokerEnvironment:
    

    
    def __init__(self):
        self.phase = 0
        self.pot_money = 0
        self.DeckofCards = ['2d','3d','4d','5d','6d','7d','8d','Td','Jd','Qd','Kd','Ad',
                    '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',
                    '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                    '2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As']
        

    def getDeckofCards(self):
        random.shuffle(self.DeckofCards)
        return self.DeckofCards

    def addToPot(self,bet):
        self.pot_money += bet

    def getPot(self):
        x = self.pot_money
        self.pot_money = 0
        self.phase=0
        return x
    
    def incrementPhase(self):
        self.phase+=1
        
    def getPhase(self):
        return self.phase
        
def assignPlayersCards(DeckofCards,player1,player2):

    Hand1 = []
    Hand2 = []
        
    for i in range(6):
        if(i<3):
            Hand1.append(DeckofCards[i])
        elif(i>=3):
            Hand2.append(DeckofCards[i])
        player1.assignCards(Hand1)
        player2.assignCards(Hand2)
       # print Hand1, Hand2
        #add hand1 to player1
        #add hand2 to player2
def compairCards(hand1,hand2):
    print "Hand1: ",hand1,"Hand2: ",hand2

    if hand1==hand2:
        return 0
    
    if(hand1>hand2):
        return 1
    elif(hand1<hand2):
        return 2
        
        

#Start the environment#           
x = PokerEnvironment()
number_of_games = 0
#Init the agents#
player1 = Poker_Agent(5000)
player2 = Poker_Agent(5000)
#Get the deck of cards that are shuffled, and assign them to the players Phase 0#

while number_of_games < 200:
    Cards = x.getDeckofCards()
    assignPlayersCards(x.getDeckofCards(),player1,player2)
    x.incrementPhase()

    #Phase 1, start betting"
    betPlayer1 = player1.Reflex_Agent(x.getPhase())
    betPlayer2 = player2.Random_Agent(x.getPhase())
    x.addToPot(betPlayer1+betPlayer2)
    x.incrementPhase()
    #Phase 2, start betting"
    betPlayer1 = player1.Reflex_Agent(x.getPhase())
    betPlayer2 = player2.Random_Agent(x.getPhase())
    x.addToPot(betPlayer1+betPlayer2)
    x.incrementPhase()
    #Phase 3, start betting"
    betPlayer1 = player1.Reflex_Agent(x.getPhase())
    betPlayer2 = player2.Random_Agent(x.getPhase())
    x.addToPot(betPlayer1+betPlayer2)
    x.incrementPhase()
    #Showndown phase#
    #player1.analyseHand()
    #player2.analyseHand()
    announcewinner = compairCards(player1.getHandStrength(),player2.getHandStrength())
    if(announcewinner==1):
       player1.addMoney(x.getPot())
    elif(announcewinner==2):
       player2.addMoney(x.getPot())
    elif(announcewinner==0):
        cash = x.getPot()/2
        player1.addMoney(cash)
        player2.addMoney(cash)
    
    number_of_games+=1
    player1.reset_hand_strength()
    player2.reset_hand_strength()
    
player1.currentMoney()
player2.currentMoney()







