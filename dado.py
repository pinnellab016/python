"""
Programma che definisce una classe 'dado' per simulare il lancio di un dado a 6 facce.
La classe fornisce funzionalità per:
- Lanciare il dado (generando un numero casuale tra 1 e 6)
- Recuperare il valore corrente del dado
- Visualizzare il numero uscito
Il blocco principale contiene un menu interattivo che permette all'utente di
lanciare il dado, visualizzare il risultato o uscire dal programma.
"""
import random
class dado:
    def _init_(self):
        self.__numero = 1
        self.lancia()
    
    def getnumero(self):
        return self.__numero
    
    def visualizza(self):
        print("Il numero uscito è: ", self.__numero)
    
    def lancia(self):
        self.__numero = random.randint(1,6)

dadino = dado()
while True:
    print("1. Lancia il dado")
    print("2. Visualizza il numero uscito")
    print("0. Esci")

    s = int(input("Scegli un opzione (1-2): "))
    match(s):
        case 1:
            dadino.lancia()
            print("Dado lanciato!")
        
        case 2:
            dadino.visualizza()
        
        case 3:
            print("Programma terminato!")
            break

        case _:
            print("Scelta non valida!")