from random import shuffle
import copy

class Karte:
    def __init__(self, bild, weich, hart, anzug ):
        self.bild=bild
        self.weich=weich
        self.hart=hart
        self.anzug=anzug

    def __repr__(self):
        return f'{self.bild}, {self.weich}, {self.hart}, {self.anzug}'
    def __str__(self):
        return f'{self.bild}, {self.weich}, {self.hart}, {self.anzug}'

class FaceCard(Karte):
    def __init__(self, bild, weich, hart, anzug):
        super().__init__(bild, weich, hart, anzug)
        self.weich=10
        self.hart=10
        super.__str__(self)



class AceCard(FaceCard):
    def __init__(self, bild, weich, hart, anzug):
        super().__init__(bild, weich, hart, anzug)

        self.weich=1
        self.hart=10
        super.__str__(self)

    def __eq__(self, other):
        return other['weich']==1 and other['hart']==10

class Deck(Karte):
    def __init__(self):
        self.cardliste=[]


    def next_card(self):
        """
        obtine urmatoarea carte din pachet
        """
        next=self.cardliste[0]
        self.cardliste.pop(0)
        return next



    def mischen(self,cardliste):
        """
        amestecarea listei de carti
        """
        shuffle(cardliste)
        return cardliste


    def initialisieren(self):
        """
        initializarea listei de carti
        """
        self.cards= [chr(code) for code in range(ord('🂡'), ord('🃞') + 1)]   #obtinerea imaginii
        self.cards = [code for code in self.cards if code not in ['', '', '🃏', '', '\U0001f0af', '\U0001f0b0', '\U0001f0c0', '\U0001f0d0', '🂬', '🂼', '🃌', '🃜', '🂿']]
        karte=Karte(" ", 0, 0, " ")
        for card in self.cards:

            karte.bild=card                                     #setarea imaginii pt fiecare carte
            if (str(card.encode()))[-3] == 'a':                 #penultimul caracter utf8 pt inima neagra=a
                karte.anzug='spades'
            elif (str(card.encode()))[-3]== 'b':                #penultimul caracter utf8 pt inima rosie=b
                karte.anzug='hearts'
            elif (str(card.encode()))[-3]== '8':                #penultimul caracter utf8 pt romb=8
                karte.anzug = 'diamonds'
            elif (str(card.encode()))[-3]=='9':                 #penultimul caracter utf8 pt trifoi=9
                karte.anzug='clubs'

            if (str(card.encode()))[-2]=='1':                   #ultimul caracter utf8 pt as=1
                karte=AceCard(karte.bild, 1, 10,  karte.anzug)
            elif (str(card.encode()))[-2] in '23456789':        #ultimul caracter utf8 corespunde valorii cartii
                karte.weich=int((str(card.encode()))[-2])
                karte.hart=int((str(card.encode()))[-2])
            elif (str(card.encode()))[-2] in 'abde':            #ultimul caracter utf8 pt 10/J/Q/K=a/b/d/e
                karte=FaceCard(karte.bild,10, 10, karte.anzug)

            new_card={'bild':copy.copy(karte.bild), 'weich':copy.copy(karte.weich), 'hart':copy.copy(karte.hart), 'anzug':copy.copy(karte.anzug)}
                #contine o copie a cartii actualizate, deoarece este obiect mutable

            self.cardliste.append(new_card)                     #adaugam cartea in lista

        Deck.mischen(self,self.cardliste)                       #amestecam pachetul

    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        return f'Karten: {self.cardliste}'











