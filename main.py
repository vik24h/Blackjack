from Deck import Deck
def test_Kartentausch():
    deck=Deck()
    deck.initialisieren()           #pachet amestecat la initializare
    card_1=deck[0]
    deck.mischen()                  #a doua amestecare
    assert card_1 != deck[0]        #dupa a doua amestecare cartea care a fost initial pe prima pozitie se afla altundeva in pachet
def test_Karte_einzigartig():
    deck=Deck()
    deck.initialisieren()
    erste=deck.next_card()
    assert erste not in deck        #dupa ce a fost luata din pachet, cartea va fi eliminata

def test_weich_hart():
    deck=Deck
    deck.initialisieren()
    for card in deck:
        if (str(card.encode()))[-2] == '1':             #as
            assert card.weich==1 and card.hart==10
        elif (str(card.encode()))[-2] in '23456789':    #carti cu valori 2-9
            assert card.weich==int((str(card.encode()))[-2]) and card.hart==int((str(card.encode()))[-2])
        elif (str(card.encode()))[-2] in 'abde':        #10/J/Q/K
            assert card.weich==10 and card.hart==10
