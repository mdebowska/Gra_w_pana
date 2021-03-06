﻿import random
from src import CardClass
from src import GameClass

names = ['Ada', 'Justyna', 'Gosia', 'Maciej', 'Wiesław', 'Krysia', 'Marian', 'John', 'Jane']

class Person:
    """
    Klasa gracza
    """
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.active = 0
        self.layed_card = []
        # add_player(self)

    def __repr__(self):
        return self.name

    def say_about_yourself(self):
        """
        Funkcja informująca o stanie gracza
        :return:
        """
        return '%s: %d kart' % (self.name, len(self.hand))
        # return 'Jestem %s, a w ręce trzymam %d kart. Są to: ' % (self.name, len(self.hand))#, str(self.hand))


    def take_card(self):
        """
        Dodanie karty z talii do ręki gracza
        :return:
        """
        card = random.choice(CardClass.all_cards)
        CardClass.all_cards.remove(card)
        self.hand.append(card)

    def check_if_winner(self):
        """
        Sprawdza, czy dany gracz wygrał
        :return:
        """
        if len(self.hand) == 0:
            return True

    def set_last_card(self, last_card):
        """
        Ustawia wybraną kartę na końcu kolejki
        :return:
        """
        # for card in self.hand:
        #     if card == last_card
        self.hand.remove(last_card)
        self.hand.append(last_card)



    def set_useful_cards(self, game):
        """
        Ustawia Trure dla użyteżcznych kart (tzn można nimi zagrać)
        :return:
        """
        for card in self.hand:
            if card.value >= game.stack[len(game.stack)-1].value:
                if len(self.layed_card) > 0:
                    if  self.layed_card[0].value == card.value:
                        card.useful = True
                        # print("usefulA: ", card)
                    else:
                        card.useful = False
                        # print("NIEusefulA: ", card)
                else:
                    card.useful = True
                    # print("usefulB: ", card)
            else:
                card.useful = False
                # print("NIEusefulC: ", card)

    def make_useful_list(self):
        """
        Tworzy listę zero-jedynkową użytecznych kart
        :return: list
        """
        useful_list=[]
        for card in self.hand:
           if card.useful:
               useful_list.append(1)
           else:
               useful_list.append(0)

        return useful_list