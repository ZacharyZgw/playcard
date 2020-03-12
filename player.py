import card
from cards import *
class Player:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards

def play(player1,player2):
    p1_tonghuashun=check_tonghuashun(player1.cards)
    p2_tonghuashun = check_tonghuashun(player2.cards)
    p1_tiezi = check_tiezhi(player1.cards)
    p2_tiezi = check_tiezhi(player2.cards)
    p1_hulu = check_hulu(player1.cards)
    p2_hulu = check_hulu(player2.cards)
    p1_tonghua = check_tonghua(player1.cards)
    p2_tonghua = check_tonghua(player2.cards)
    p1_shunzi = check_shunzi(player1.cards)
    p2_shunzi = check_shunzi(player2.cards)
    p1_three = check_three(player1.cards)
    p2_three = check_three(player2.cards)
    p1_two_pair = check_two_pair(player1.cards)
    p2_two_pair = check_two_pair(player2.cards)
    p1_pair = check_pair(player1.cards)
    p2_pair = check_pair(player2.cards)
    #print(p1_tonghuashun,p2_tonghuashun,p1_tiezi,p2_tiezi,p1_hulu,p2_hulu,p1_three,p2_three)
    if p1_tonghuashun and p2_tonghuashun==False:
        return "同花顺 {name} wins".format(player1.name)
    elif p1_tonghuashun==False and p2_tonghuashun:
        return "同花顺 {name} wins".format(player2.name)
    elif p1_tonghuashun and p2_tonghuashun:
        _,player1_max_card = check_shunzi(player1.cards)
        _,player2_max_card = check_shunzi(player2.cards)
        if player1_max_card > player2_max_card:return "同花顺 {name} wins".format(name=player1.name)
        if player1_max_card < player2_max_card:return "同花顺 {name} wins".format(name=player2.name)
        if player1_max_card == player2_max_card:return "同花顺 平局"
    else:
        if p1_tiezi and p2_tiezi==False:
            return "铁支 {name} wins".format(name=player1.name)
        elif p1_tiezi==False and p2_tiezi:
            return "铁支 {name} wins".format(name=player2.name)
        elif p1_tiezi and p2_tiezi:
            _,player1_card_value = check_tiezhi(player1.cards)
            _,player2_card_value = check_tiezhi(player2.cards)
            if player1_card_value > player2_card_value:return "铁支 {name} wins".format(name=player1.name)
            if player1_card_value < player2_card_value:return "铁支 {name} wins".format(name=player2.name)
            if player1_card_value == player2_card_value:return "铁支 平局"
        else:
            if p1_hulu and p2_hulu==False:
                return "葫芦 {name} wins".format(name=player1.name)
            elif p1_hulu==False and p2_hulu:
                return "葫芦 {name} wins".format(name=player2.name)
            elif p1_hulu and p2_hulu:
                _,player1_card_value,_ = check_three(player1.cards)
                _,player2_card_value,_ = check_three(player2.cards)
                if player1_card_value > player2_card_value: return "葫芦 {name} wins".format(name=player1.name)
                if player1_card_value < player2_card_value: return "葫芦 {name} wins".format(name=player2.name)
                if player1_card_value == player2_card_value: return "葫芦 平局"
            else:
                if p1_tonghua and p2_tonghua==False:
                    return "同花 {name} wins".format(name=player1.name)
                elif p1_tonghua==False and p2_tonghua:
                    return "同花 {name} wins".format(name=player2.name)
                elif p1_tonghua and p2_tonghua:
                    _, player1_sum, _ = check_tonghua(player1.cards)
                    _, player2_sum, _ = check_tonghua(player2.cards)
                    if player1_sum > player2_sum: return "同花 {name} wins".format(name=player1.name)
                    if player1_sum < player2_sum: return "同花 {name} wins".format(name=player2.name)
                    if player1_sum == player2_sum: return "同花 平局"
                else:
                    if p1_shunzi and p2_shunzi == False:
                        return "顺子 {name} wins".format(name=player1.name)
                    elif p1_shunzi == False and p2_shunzi:
                        return "顺子 {name} wins".format(name=player2.name)
                    elif p1_shunzi and p2_shunzi:
                        _, player1_card_value = check_shunzi(player1.cards)
                        _, player2_card_value = check_shunzi(player2.cards)
                        if player1_card_value > player2_card_value: return "顺子 {name} wins".format(name=player1.name)
                        if player1_card_value < player2_card_value: return "顺子 {name} wins".format(name=player2.name)
                        if player1_card_value == player2_card_value: return "顺子 平局"
                    else:
                        if p1_three and p2_three == False:
                            return "三条 {name} wins".format(name=player1.name)
                        elif p1_three == False and p2_three:
                            return "三条 {name} wins".format(name=player2.name)
                        elif p1_three and p2_three:
                            _, player1_card_value,_ = check_three(player1.cards)
                            _, player2_card_value,_ = check_three(player2.cards)
                            if player1_card_value > player2_card_value: return "三条 {name} wins".format(name=player1.name)
                            if player1_card_value < player2_card_value: return "三条 {name} wins".format(name=player2.name)
                            if player1_card_value == player2_card_value: return "三条 平局"
                        else:
                            if p1_two_pair and p2_two_pair == False:
                                return "两对 {name} wins".format(name=player1.name)
                            elif p1_two_pair == False and p2_two_pair:
                                return "两对 {name} wins".format(name=player2.name)
                            elif p1_two_pair and p2_two_pair:
                                _, player1_min_value,player1_max_value, player1_rest_value = check_two_pair(player1.cards)
                                _, player2_min_value,player2_max_value, player2_rest_value = check_three(player2.cards)
                                if player1_max_value > player2_max_value:
                                    return "两对 {name} wins".format(name=player1.name)
                                elif player2_max_value >player1_max_value:
                                    return "两对 {name} wins".format(name=player2.name)
                                elif player1_max_value == player2_max_value:
                                    if player1_min_value > player2_min_value:
                                        return "两对 {name} wins".format(name=player1.name)
                                    elif player1_min_value < player2_min_value:
                                        return "两对 {name} wins".format(name=player2.name)
                                    elif player1_min_value == player2_min_value:
                                        if player1_rest_value>player2_rest_value:
                                            return "两对 {name} wins".format(name=player1.name)
                                        elif player1_rest_value<player2_rest_value:
                                            return "两对 {name} wins".format(name=player2.name)
                                        else:return "两对 平局"
                            else:
                                if p1_pair and p2_pair == False:
                                    return "对子 {name} wins".format(name=player1.name)
                                elif p1_pair == False and p2_pair:
                                    return "对子 {name} wins".format(name=player2.name)
                                elif p1_pair and p2_pair:
                                    _, player1_aim_value,player1_rest_value = check_pair(player1.cards)
                                    _, player2_aim_value,player2_rest_value = check_pair(player2.cards)
                                    if player1_aim_value > player2_aim_value:
                                        return "对子 {name} wins".format(name=player1.name)
                                    elif player2_aim_value > player1_aim_value:
                                        return "对子 {name} wins".format(name=player2.name)
                                    elif player1_aim_value == player2_aim_value:
                                        if player1_rest_value > player2_rest_value:
                                            return "对子 {name} wins".format(name=player1.name)
                                        elif player1_rest_value < player2_rest_value:
                                            return "对子 {name} wins".format(name=player2.name)
                                        else:return "对子 平局"
                                else:
                                    player1.cards.sort(key=lambda x: x.real_value)
                                    player2.cards.sort(key=lambda x: x.real_value)
                                    if player1.cards[-1].real_value > player2.cards[-1].real_value:
                                        return "散牌 {name} wins high card {val}".format(name=player1.name,val=player1.cards[-1].value)
                                    elif player1.cards[-1].real_value < player2.cards[-1].real_value:
                                        return "散牌 {name} wins high card {val}".format(name=player2.name,val=player2.cards[-1].value)
                                    elif player1.cards[-1].real_value == player2.cards[-1].real_value:
                                        if player1.cards[-2].real_value > player2.cards[-2].real_value:
                                            return "散牌 {name} wins high card {val}".format(name=player1.name,val=player1.cards[-2].value)
                                        elif player1.cards[-2].real_value < player2.cards[-2].real_value:
                                            return "散牌 {name} wins high card {val}".format(name=player2.name,val=player2.cards[-2].value)
                                        elif player1.cards[-2].real_value == player2.cards[-2].real_value:
                                            if player1.cards[2].real_value > player2.cards[2].real_value:
                                                return "散牌 {name} wins high card {val}".format(name=player1.name,val=player1.cards[2].value)
                                            elif player1.cards[2].real_value < player2.cards[2].real_value:
                                                return "散牌 {name} wins high card {val}".format(name=player2.name,val=player2.cards[2].value)
                                            elif player1.cards[2].real_value == player2.cards[2].real_value:
                                                if player1.cards[1].real_value > player2.cards[1].real_value:
                                                    return "散牌 {name} wins high card {val}".format(name=player1.name,val=player1.cards[1].value)
                                                elif player1.cards[1].real_value < player2.cards[1].real_value:
                                                    return "散牌 {name} wins high card {val}".format(name=player2.name,val=player2.cards[1].value)
                                                elif player1.cards[1].real_value == player2.cards[1].real_value:
                                                    if player1.cards[0].real_value > player2.cards[0].real_value:
                                                        return "散牌 {name} wins high card {val}".format(name=player1.name,val=player1.cards[0].value)
                                                    elif player1.cards[0].real_value < player2.cards[0].real_value:
                                                        return "散牌 {name} wins high card {val}".format(name=player2.name,val=player2.cards[0].value)
                                                    else:return "散牌 平局"



                                    else:
                                        return "散牌 平局"
def card_type(five_cards):
    if check_tonghuashun(five_cards):
        return '同花顺'
    elif check_tiezhi(five_cards):
        return '铁支'
    elif check_hulu(five_cards):
        return '葫芦'
    elif check_tonghua(five_cards):
        return '同花'
    elif check_shunzi(five_cards):
        return "顺子"
    elif check_three(five_cards):
        return '三条'
    elif check_two_pair(five_cards):
        return '两对'
    elif check_pair(five_cards):
        return '对子'
    else:
        return '散牌'

if __name__ == "__main__":
    c11 = Card("H", 2, 1)
    c12 = Card("D", 3, 2)
    c13 = Card("S", 5, 4)
    c14 = Card("C", 9, 8)
    c15 = Card("D", 'K', 12)
    player1 = Player('black', [c11, c12, c13, c14, c15])
    c21 = Card("C", 2, 1)
    c22 = Card("H", 3, 2)
    c23 = Card("S", 4, 3)
    c24 = Card("C", 8, 7)
    c25 = Card("H", 'A', 13)
    player2 = Player('white', [c21, c22, c23, c24, c25])
    #print(check_tiezhi(player2.cards))
    print('player1 {}'.format(player1.name),end=": ")
    for card in player1.cards:
        print("{}{}".format(card.color,card.value),end=" ")
    print(card_type(player1.cards))
    print()
    print('player2 {}'.format(player2.name),end=": ")
    for card in player2.cards:
        print("{}{}".format(card.color,card.value),end=" ")
    print(card_type(player2.cards))
    print()
    print(play(player1,player2))



