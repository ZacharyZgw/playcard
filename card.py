class Card:
    def __init__(self,color,value,real_value):
        self.color = color
        self.value = value
        self.real_value = real_value
        self.all_cards = []
    def __str__(self):
        return "{color}{value}{real_value}".format(color=self.color,value = self.value,real_value=self.real_value)
    def init_cards(self):
        values = [i for i in range(2,11)]
        values.extend(['j','Q','K','A'])
        for color in "♥♠♦♣":
            count = 1
            for j in values:
                card = Card(color,j,count)
                self.all_cards.append(card)
                count+=1

if __name__ =="__main__":
    card = Card()
    card.init_cards()
    print(card.all_cards)
