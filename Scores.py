from datetime import date

class Scores:
    def __init__(self):
        self.datum=date.today()
        self.nr_runden=5
        self.spieler_name=[]
        self.geld=[]
        self.spieler_score=[]
        self.dealer_score=[]

    def read_scores(self):
        """
        citeste rezultatele din fisier si le afiseaza sortate in functie de rezultatul jucatorului

        informatiile din fisier sub format: Nume jucator, Scor jucator, Bani jucator, Scor dealer
        """
        ergebnisse=[]
        file=open("Blackjack.txt", 'r')
        for line in file.readlines():
            ergebnisse.append(tuple(line.rstrip().split(',')))              #o lista de tuples, care contin informatiile din fisier delimitate cu virgula
        file.close()

        ergebnisse.sort(key=lambda spieler: int(spieler[1]), reverse=True)  #sortare in functie de rezultatul jucatorului

        for  a_tuple in ergebnisse:                                         #liste separate pentru nume, scor si bani pentru a putea afisa corespunzator pt jucatori diferiti
            self.spieler_score.append(a_tuple[1])
            self.dealer_score.append(a_tuple[3])
            self.spieler_name.append(a_tuple[0])
            self.geld.append(a_tuple[2])



    def add_score(self, name_spieler,ergebnis_spieler,geld_spieler, ergebnis_dealer) :
        """
        adauga rezultatul jocului in fisier sub formatul: Nume jucator, Scor jucator, Bani jucator, Scor dealer
        """
        file=open("Blackjack.txt", 'a')
        file.write(str(name_spieler) + ", "+ str(ergebnis_spieler) +", " + str(geld_spieler) + ", " + str(ergebnis_dealer) +"\n")
        file.close()

    def __repr__(self):
        return f'{self.datum}  {self.nr_runden}  {self.spieler_name}: {self.spieler_score}, {self.geld}, Dealer: {self.dealer_score} \n'
    def __str__(self):
        return f'{self.datum}  {self.nr_runden}  {self.spieler_name}: {self.spieler_score}, {self.geld}, Dealer: {self.dealer_score} '

