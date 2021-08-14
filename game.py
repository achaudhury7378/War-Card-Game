import os
import random as r
def deal():

    cards=[]
    player_1_hand=[]
    values=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for i in values:
        for _ in range(4):
            cards.append(i)
    r.shuffle(cards)
    for i in range(26):
        card=r.choice(cards)
        player_1_hand.append(card)
        card_index=cards.index(card)
        cards.pop(card_index)
    player_2_hand=[x for x in cards]
    '''
    Test cases:

    Full draw game :
    
    player_2_hand=['A','J','2','8','9','7','5','8','9','K','Q','A','9']
    player_1_hand=['A','J','7','7','9']
    
    Draw hand single:
    player_2_hand=['A','J','2','8','10','7','5','8','9','K','Q','A','8']
    player_1_hand=['A','J','7','7','9']

    Draw hand double:
    player_2_hand=['A','J','2','8','9','7','5','8','9','K','Q','A','8']
    player_1_hand=['A','J','7','7','9']
    '''
    return player_1_hand,player_2_hand
def result(move_1,move_2):
    rankings={'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13}
    if rankings[move_1]>rankings[move_2]:
        return 1
    elif rankings[move_1]<rankings[move_2]:
        return 2
    elif rankings[move_1]==rankings[move_2]:
        return 3
class Player:
    def __init__(self,name,at_hand):
        self.at_hand=at_hand
        self.name=name
    def play(self):
        return self.at_hand.pop(0)
    def add_to_hand(self,move):
        for i in move:
            self.at_hand.append(i)
        return self.at_hand
def play_draw(Player_1_war_hand,Player_2_war_hand):
    if len(Player_1.at_hand)>=4 and len(Player_2.at_hand)>=4:
        for _ in range(3):
            Player_1_war_hand.append(Player_1.play())
            Player_2_war_hand.append(Player_2.play())
        move_1=Player_1.play()
        move_2=Player_2.play()
        if result(move_1,move_2)==1:
            Player_1.add_to_hand([move_1,move_2])
            Player_1.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_1.name," wins")
            Player_1_war_hand=[]
            Player_2_war_hand=[]
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
        elif result(move_1,move_2)==2:
            Player_2.add_to_hand([move_1,move_2])
            Player_2.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_2.name," wins")
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
            Player_1_war_hand=[]
            Player_2_war_hand=[]
        elif result(move_1,move_2)==3:
            Player_1_war_hand.append(move_1)
            Player_2_war_hand.append(move_2)
            play_draw(Player_1_war_hand,Player_2_war_hand)
    elif len(Player_1.at_hand)>=4 and len(Player_2.at_hand)<=3:
        for _ in range(3):
            Player_1_war_hand.append(Player_1.play())
        for _ in range(len(Player_2.at_hand)-1):
            Player_2_war_hand.append(Player_2.play())
        move_1=Player_1.play()
        try :
            move_2=Player_2.play()
        except:
            move_2=Player_2_war_hand.pop(-1)
        if result(move_1,move_2)==1:
            Player_1.add_to_hand([move_1,move_2])
            Player_1.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_1.name," wins")
            Player_1_war_hand=[]
            Player_2_war_hand=[]
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
        elif result(move_1,move_2)==2:
            Player_2.add_to_hand([move_1,move_2])
            Player_2.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_2.name," wins")
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
            Player_1_war_hand=[]
            Player_2_war_hand=[]
        elif result(move_1,move_2)==3:
            Player_1_war_hand.append(move_1)
            Player_2_war_hand.append(move_2)
            play_draw(Player_1_war_hand,Player_2_war_hand)
    elif len(Player_1.at_hand)<=3 and len(Player_2.at_hand)>=4:
        for _ in range(3):
            Player_2_war_hand.append(Player_2.play())
        for _ in range(len(Player_1.at_hand)-1):
            Player_1_war_hand.append(Player_1.play())
        move_2=Player_2.play()
        try :
            move_1=Player_1.play()
        except:
            move_1=Player_1_war_hand.pop(-1)
        if result(move_1,move_2)==1:
            Player_1.add_to_hand([move_1,move_2])
            Player_1.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_1.name," wins")
            Player_1_war_hand=[]
            Player_2_war_hand=[]
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
        elif result(move_1,move_2)==2:
            Player_2.add_to_hand([move_1,move_2])
            Player_2.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_2.name," wins")
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
            Player_1_war_hand=[]
            Player_2_war_hand=[]
        elif result(move_1,move_2)==3:
            Player_1_war_hand.append(move_1)
            Player_2_war_hand.append(move_2)
            play_draw(Player_1_war_hand,Player_2_war_hand)
    elif len(Player_1.at_hand)<=3 and len(Player_2.at_hand)<=3:
        for _ in range(len(Player_1.at_hand)-1):
            Player_1_war_hand.append(Player_1.play())
        for _ in range(len(Player_2.at_hand)-1):
            Player_2_war_hand.append(Player_2.play())
        try :
            move_1=Player_1.play()
            move_2=Player_2.play()
        except:
            move_1=Player_1_war_hand.pop(-1)
            move_2=Player_2_war_hand.pop(-1)
        if result(move_1,move_2)==1:
            Player_1.add_to_hand([move_1,move_2])
            Player_1.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_1.name," wins")
            Player_1_war_hand=[]
            Player_2_war_hand=[]
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
        elif result(move_1,move_2)==2:
            Player_2.add_to_hand([move_1,move_2])
            Player_2.at_hand.extend(Player_1_war_hand+Player_2_war_hand)
            print(Player_2.name," wins")
            #print(Player_1.at_hand)
            #print(Player_2.at_hand)
            Player_1_war_hand=[]
            Player_2_war_hand=[]
        elif result(move_1,move_2)==3:
            global a
            a=4
print("Welcome to WAR card game")
name_1=input('Player 1 : ')
name_2=input("Player 2 : ")
Players=[]
Players.append(name_1)
Players.append(name_2)
player_1_hand,player_2_hand=deal()
Player_1=Player(name_1,player_1_hand)
Player_2=Player(name_2,player_2_hand)
turn=0
resume='T'
os.system('cls')
a=0
while True:
    print('You have asked for a move "--play" or "--help"',Players[turn%2])
    move=input()
    if move=="--play":
        if turn%2 ==0:
            move_player_1=0
            print(Player_1.name)
            move_player_1=Player_1.play()
            #print(Player_1.at_hand)
            print(move_player_1)
            turn=turn+1
        elif turn%2==1:
            print(Player_2.name)
            move_player_2=Player_2.play()
            #print(Player_2.at_hand)
            print(move_player_2)
            turn=turn+1
        if turn%2==0:
            if result(move_player_1,move_player_2)==1:
                Player_1.add_to_hand([move_player_1,move_player_2])
                print(Player_1.name," wins")
                #print(Player_1.at_hand)
                #print(Player_2.at_hand)
            elif result(move_player_1,move_player_2)==2:
                Player_2.add_to_hand([move_player_1,move_player_2])
                print(Player_2.name," wins")
                #print(Player_1.at_hand)
                #print(Player_2.at_hand)
            elif result(move_player_1,move_player_2)==3:
                play_draw(Player_1_war_hand=[move_player_1],Player_2_war_hand=[move_player_2])
    if len(Player_1.at_hand)==52 or len(Player_2.at_hand)==52:
        if len(Player_1.at_hand)==52:
            print(Player_1.name,'wins the game')
            break  
        elif len(Player_2.at_hand)==52:
            print(Player_2.name,'wins the game')
            break
    if a==4:
        print('game draw')
        break
    elif move=="--help":
        os.system('cls')
        fin=open('help.txt','r')
        lines=fin.readlines()
        for line in lines:
            print(line[:-1])
        fin.close()
        while resume!='--resume':
            resume=input("Do you want to resume ?")
            if resume=='--resume':
                os.system('cls')
                break
            else:
                print("please enter '--resume'")
