import pytest
import card
from cards import *
from player import *

#测试数据
'''
Card(color,value,real_value)
color:花色 方片 D 黑桃 S 红桃 H 梅花 C
value:字面值:2 3 4 5 6 7 8 9 10 J Q K A
真实值：1，2，3，4，5，6，7，8，9，10，11，12，13

'''
c11_0=Card("H",2,1)
c12_0=Card("D",3,2)
c13_0=Card("S",5,4)
c14_0=Card("C",9,8)
c15_0=Card("D",'K',12)
player1_0 = Player('black',[c11_0,c12_0,c13_0,c14_0,c15_0])
c21_0 = Card("C", 2, 1)
c22_0 = Card("H", 3, 2)
c23_0 = Card("S", 4, 3)
c24_0 = Card("C", 8, 7)
c25_0 = Card("H", 'A', 13)
player2_0 = Player('white', [c21_0, c22_0, c23_0, c24_0, c25_0])


def test_player1_card_type(player=player1_0):
    cards = player.cards
    assert card_type(cards) == '散牌'

def test_player2_card_type(player=player2_0):
    cards = player.cards
    assert card_type(cards) == '散牌'
def test_play(player1=player1_0,player2=player2_0):
    assert play(player1,player2) == '散牌 white wins high card A'

c11_1=Card("H",2,1)
c12_1=Card("S",4,3)
c13_1=Card("C",4,3)
c14_1=Card("D",2,1)
c15_1=Card("H",4,3)
player1_1 = Player('black',[c11_1,c12_1,c13_1,c14_1,c15_1])
c21_1 = Card("S", 2, 1)
c22_1 = Card("S", 8, 7)
c23_1 = Card("S", 'A', 13)
c24_1 = Card("S", 'Q', 11)
c25_1 = Card("S", 3, 2)
player2_1 = Player('white', [c21_1, c22_1, c23_1, c24_1, c25_1])

def test_player1_card_type1(player=player1_1):
    cards = player.cards
    assert card_type(cards) == '葫芦'

def test_player2_card_type1(player=player2_1):
    cards = player.cards
    assert card_type(cards) == '同花'
def test_play1(player1=player1_1,player2=player2_1):
    assert play(player1,player2) == '葫芦 black wins'

c11_2=Card("H",2,1)
c12_2=Card("D",3,2)
c13_2=Card("S",5,4)
c14_2=Card("C",9,8)
c15_2=Card("D",'K',12)
player1_2 = Player('black',[c11_2,c12_2,c13_2,c14_2,c15_2])
c21_2 = Card("C", 2, 1)
c22_2 = Card("H", 3, 2)
c23_2 = Card("S", 4, 3)
c24_2 = Card("C", 8, 7)
c25_2 = Card("H", 'k', 12)
player2_2 = Player('white', [c21_2, c22_2, c23_2, c24_2, c25_2])

def test_player1_card_type2(player=player1_2):
    cards = player.cards
    assert card_type(cards) == '散牌'

def test_player2_card_type2(player=player2_2):
    cards = player.cards
    assert card_type(cards) == '散牌'
def test_play2(player1=player1_2,player2=player2_2):
    assert play(player1,player2) == '散牌 black wins high card 9'

c11_3=Card("H",2,1)
c12_3=Card("D",3,2)
c13_3=Card("S",5,4)
c14_3=Card("C",9,8)
c15_3=Card("D",'K',12)
player1_3 = Player('black',[c11_3,c12_3,c13_3,c14_3,c15_3])
c21_3 = Card("D", 2, 1)
c22_3 = Card("H", 3, 2)
c23_3 = Card("C", 5, 4)
c24_3 = Card("S", 9, 8)
c25_3 = Card("H", 'k', 12)
player2_3 = Player('white', [c21_3, c22_3, c23_3, c24_3, c25_3])

def test_player1_card_type3(player=player1_3):
    cards = player.cards
    assert card_type(cards) == '散牌'

def test_player2_card_type3(player=player2_3):
    cards = player.cards
    assert card_type(cards) == '散牌'
def test_play3(player1=player1_3,player2=player2_3):
    assert play(player1,player2) == '散牌 平局'