"""
Programma che definisce una classe Quadrato e ne mostra l'uso.
La classe gestisce il lato, il calcolo dell'area e del perimetro,
consente di modificare il lato e verifica che il lato sia positivo.
Nel blocco principale viene creato un quadrato, stampati i valori
calcolati e richiesto un nuovo lato dall'utente.
"""

class Quadrato:
    def __init__(self, lato):
        """Costruttore"""
        self.lato = lato
    
    def __del__(self):
        """Distruttore"""
        print(f"Quadrato con lato {self.lato} eliminato")
    
    def get_lato(self):
        """Getter per il lato"""
        return self.lato
    
    def set_lato(self, lato):
        """Setter per il lato"""
        if lato > 0:
            self.lato = lato
        else:
            print("Il lato deve essere positivo")
    
    def get_area(self):
        """Calcola l'area"""
        return self.lato ** 2
    
    def get_perimetro(self):
        """Calcola il perimetro"""
        return self.lato * 4
    
# esempio di utilizzo
if __name__ == "__main__":
    q = Quadrato(5)                     # istanzia un quadrato di lato 5
    print("Lato:", q.get_lato())
    print("Area:", q.get_area())
    print("Perimetro:", q.get_perimetro())

    q.set_lato(3)                       # modifica il lato
    print("Nuovo lato:", q.get_lato())
    print("Nuova area:", q.get_area())
    print("Nuovo perimetro:", q.get_perimetro())

    q.set_lato(-1)                      # prova un valore non valido

    # il distruttore verrà chiamato all'uscita dal programma

    l = int(input("Inserisci il valore del lato: "))
    q1 = Quadrato(l)                     # istanzia un nuovo quadrato con il lato inserito

    print( "AREA QUADRATO q1: ", q1.get_area() )