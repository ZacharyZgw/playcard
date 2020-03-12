from card import *
import random
class Cards:
    def __init__(self):
        self.all_cards = []
        self.five_cards = []
        self.type = None

    def init_cards(self):
        values = list(range(2, 11)) + list("JQKA")
        for color in "DSHC":
            count = 1
            for i in values:
                c = Card(color, i,  count)
                self.all_cards.append(c)
                count += 1
    def get_five_cards(self):
        for i in range(5):
            index = random.randint(0, len(self.all_cards) - 1)
            card = self.all_cards.pop(index)
            self.five_cards.append(card)
        return self.five_cards
    def card_type(self):
        self.five_cards.sort(key=lambda x:x.real_value)
        c0 = self.five_cards[0]
        c1 = self.five_cards[1]
        c2 = self.five_cards[2]
        c3 = self.five_cards[3]
        c4 = self.five_cards[4]
        if c0.color == c1.color == c2.color == c3.color ==c4.color:
            type=6 #同花为6
        elif c0.value == c1.value == c2.value ==c3.value ==c4.value:
            type = 4 #三条为4
        elif c0.value == c1.value or c0.value == c2.value or\
            c0.value == c3.value or c0.value==c4.value or\
            c1.value == c2.value or c1.value== c3.value or c1.value == c4.value or\
            c2.value == c3.value or c2.value==c4.value or c3.value ==c4.value:
            type = 2 #对子为2
def get_frequencies(objs,keyword):
    frequencies = {}  # 统计相同牌的个数
    for card in objs:
        if card.keyword not in frequencies:
            frequencies[card.keyword] = 1
        else:
            frequencies[card.keyword] += 1
    return frequencies
#检测是不是对子
def check_pair(five_cards):
    frequencies = {} #统计相同牌的个数
    for card in five_cards:
        if card.real_value not in frequencies:
            frequencies[card.real_value]=1
        else:
            frequencies[card.real_value]+=1
    count = [i for i in frequencies.values()]
    if count.count(2) ==1:
        aim_card = [card for card in five_cards if frequencies[card.real_value]==2]
        aim_card_value = aim_card[0].real_value
        rest_card_value = sum([rest_card.real_value for rest_card in five_cards if frequencies[rest_card.real_value] == 1])
        return True,aim_card_value,rest_card_value
    else:
        return False
#检测是不是两对
def check_two_pair(five_cards):
    frequencies = {}
    for card in five_cards:
        if card.real_value not in frequencies:
            frequencies[card.real_value] =1
        else:
            frequencies[card.real_value]+=1
    count = [i for i in frequencies.values()]
    if count.count(2) ==2:
        aim_card = [card for card in five_cards if frequencies[card.real_value]==2]
        min_value = min([card.real_value for card in aim_card])
        max_value = max([card.real_value for card in aim_card])
        rest_card = [rest_card for rest_card in five_cards if frequencies[rest_card.real_value] == 1]
        return True,min_value,max_value,rest_card[0].real_value
    else:
        return False
#检测是不是三条
def check_three(five_cards):
    frequencies = {}
    for card in five_cards:
        if card.real_value not in frequencies:
            frequencies[card.real_value]=1
        else:
            frequencies[card.real_value]+=1
    count = [i for i in frequencies.values()]
    if count.count(3)==1:
        aim_card = [card for card in five_cards if frequencies[card.real_value]==3]
        card_value = aim_card[0].real_value
        rest_cards = [card for card in five_cards if frequencies[card.real_value]!=3]
        return True,card_value,rest_cards
    else:
        return False
#检测是不是顺子
def check_shunzi(five_cards):
    five_cards.sort(key=lambda x:x.real_value)
    frequencies = {}
    for card in five_cards:
        if card.real_value not in frequencies:
            frequencies[card.real_value]=1
        else:
            frequencies[card.real_value]+=1
    count = [i for i in frequencies.values()]
    if count.count(1)==5 and five_cards[4].real_value-five_cards[3].real_value==1 and\
        five_cards[3].real_value-five_cards[2].real_value==1 and \
        five_cards[2].real_value - five_cards[1].real_value == 1 and \
        five_cards[1].real_value - five_cards[0].real_value == 1:
        max_card = five_cards[4].real_value
        return True,max_card
    else:
        return False
def check_tonghua(five_cards):
    five_cards.sort(key=lambda x: x.real_value)
    frequencies = {}
    for card in five_cards:
        if card.color not in frequencies:
            frequencies[card.color] = 1
        else:
            frequencies[card.color] += 1
    count = [i for i in frequencies.values()]
    sum1 = sum([card.real_value for card in five_cards])
    if count.count(5)==1:
        return True,sum1
    else:
        return False

def check_hulu(five_cards):
    if check_three(five_cards) and check_pair(five_cards):
        return True
    else:
        return False
def check_tiezhi(five_cards):
    frequencies = {}
    for card in five_cards:
        if card.real_value not in frequencies:
            frequencies[card.real_value] = 1
        else:
            frequencies[card.real_value] += 1
    count = [i for i in frequencies.values()]
    if count.count(4)==1:
        aim_card = [card for card in five_cards if frequencies[card.real_value] == 4]
        card_value = aim_card[0].real_value
        return True,card_value
    else:
        return False
def check_tonghuashun(five_cards):
    if check_shunzi(five_cards) and check_tonghua(five_cards):
        return True
    else:
        return False








if __name__ == "__main__":
    cards = Cards()
    cards.init_cards()
    for i in cards.all_cards:
        print(i)
    # print("**************")
    # c = cards.get_five_cards()
    # for j in c:
    #     print(j)
    c1 = Card('C',2,1)
    c2 = Card('C',3,2)
    c3 = Card('C',4,3)
    c4 = Card('C',5,4)
    c5 = Card('C',6,5)
    cards = [c1,c2,c3,c4,c5]
    fre= check_tonghuashun(cards)
    print(fre)
    #print(value)
    #print(fre1)
