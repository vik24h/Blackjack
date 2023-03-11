from Deck import Deck

class Dealer:
    def __init__(self):
        self.deck=Deck()

    def next_card(self):
        """
        obtine urmatoarea carte din pachet
        """
        return self.deck.next_card()


    def new_deck(self):
        """
        obtine un nou teanc de carti
        """
        self.deck.initialisieren()
        return self.deck


    def __repr__(self):
        return f'{self.bild}, {self.weich}, {self.hart}, {self.anzug}'
    def __str__(self):
        return f'Karten: {self.cardliste}'
