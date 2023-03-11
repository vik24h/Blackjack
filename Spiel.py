from Nutzer import Nutzer
from Dealer import Dealer
from Deck import AceCard, Karte
from Scores import Scores

class Spiel():
    def __init__(self, spieler):
        self.spieler=spieler
        self.dealer=Dealer()
        self.spieler_punkte=0
        self.dealer_punkte=0
        self.deck=self.dealer.new_deck()

    def __repr__(self):
        return f'{self.bild}, {self.weich}, {self.hart}, {self.anzug}'
    def __str__(self):
        return f'{self.bild}, {self.weich}, {self.hart}, {self.anzug}'


    def Runde_Spieler(self):
        """
        jucatorul alege cate carti doreste sa ia
        se intrerupe automat cand punctajul depaseste 21
        pentru cartea as, alege intre valorile 1 si 11
        """

        if self.spieler.geld-self.spieler.gespieltes_geld<0:
            raise ValueError("Nicht genug Geld zur Verfugung")

        self.next_card=self.deck.next_card()                #prima carte
        print(self.next_card)

        if AceCard.__eq__(AceCard, self.next_card):         #daca este as, alege intre 1 si 11
            value=int(input("1 oder 11?"))
            if value!=1 and value!=11:
                raise ValueError("1 oder 11 auswahlen!")
            else:
                self.spieler_punkte+=value

        else:
            self.spieler_punkte+=self.next_card['weich']    #altfel, jucatorul primeste numarul corespunzator de puncte

        print("Aktuelles Ergebnis= " + str(self.spieler_punkte))
        antwort=str(input("Noch eine Karte? (Ja/Nein) "))

        if antwort!="Ja" and antwort!="Nein":
            raise ValueError("Mit Ja oder Nein antworten")

        else:
            while antwort=="Ja" and self.spieler_punkte<21:                        #cat timp doreste sa mai ia carti, algoritmul continua pe acelasi principiu
                self.next_card = self.deck.next_card()
                print(self.next_card)

                if AceCard.__eq__(AceCard, self.next_card):
                    value = int(input("1 oder 11?"))
                    if value != 1 and value != 11:
                        raise ValueError("1 oder 11 auswahlen!")
                    else:
                        self.spieler_punkte += value

                else:
                    self.spieler_punkte += self.next_card['weich']

                print("Aktuelles Ergebnis= " + str(self.spieler_punkte))
                antwort = str(input("Noch eine Karte? (Ja/Nein) "))

                if antwort != "Ja" and antwort != "Nein":
                    raise ValueError("Mit Ja oder Nein antworten")


    def Runde_Dealer(self):
        """
        dealer-ul joaca dupa ce jucatorul a terminat
        este obligat sa traga carti cat timp are mai putin de 17 puncte, apoi este alegerea lui
        alege valoarea asului intre 1 si 11 in functie de cea mai benefica optiune
        """
        while self.dealer_punkte<17:                    #obligativitate punctaj<17
            self.next_card = self.deck.next_card()
            print(self.next_card)
            if AceCard.__eq__(AceCard, self.next_card):
                if self.dealer_punkte <= 10:            #cea mai benefica valoare pt as
                    self.dealer_punkte += 11
                else:
                    self.dealer_punkte += 1
            else:
                self.dealer_punkte += self.next_card['weich']

        while self.dealer_punkte<=21:                   #alegerea sa
            self.next_card = self.deck.next_card()
            print(self.next_card)
            if AceCard.__eq__(AceCard, self.next_card):
                if self.dealer_punkte <= 10:
                    self.dealer_punkte += 11
                else:
                    self.dealer_punkte += 1
            else:
                self.dealer_punkte += self.next_card['weich']

        print(self.dealer_punkte)
        self.deck=self.dealer.new_deck()            #dupa fiecare runda obtine un nou pachet complet si amestecat


    def Geld_Spieler(self):
        """
        calculeaza suma castigata/pierduta de jucator
        cazul de egalitate nu este tratat explicit, pt ca suma nu se modifica in acel caz
        """
        if (self.spieler_punkte>self.dealer_punkte and self.spieler_punkte<=21) or self.spieler_punkte==21 or self.dealer_punkte>21:
            self.spieler.geld+=(self.spieler.gespieltes_geld*2)     #suma se dubleaza
        elif self.spieler_punkte<self.dealer_punkte and self.dealer_punkte<=21:
            self.spieler.geld-=self.spieler.gespieltes_geld         #pierde suma jucata
        print("Geldbetrag= " + str(self.spieler.geld))


def main():
    print(
        """
            0. Exit
            1. Blackjack spielen
            2. Ergebnisse anzeigen
        """
    )


    opt=int(input("Auswahl: "))
    if opt==0:
        return 0
    if opt==1:
        spieler = Nutzer(str(input("Name: ")), int(input("Geld zu spielen: ")))
        for runden in range(1,6):           #5 runde
            partide=Spiel(spieler)
            partide.Runde_Spieler()         #randul jucatorului urmat de cel al dealer-ului
            partide.Runde_Dealer()
            partide.Geld_Spieler()          #afisarea sumei dupa fiecare joc
            Scores.add_score(Scores,spieler.name,partide.spieler_punkte,spieler.geld,partide.dealer_punkte) #incarcarea rezultatelor in fisier
    if opt==2:
        ergebnis=Scores()   #afisarea rezultatelor
        ergebnis.read_scores()
        print(ergebnis)
    elif str(opt) not in '012':
        raise ValueError("0-1 auswahlen")

main()









