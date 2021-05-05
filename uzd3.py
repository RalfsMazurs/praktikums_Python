 """
    Funkcija Bilde akceptē divus argumentus - skaiļus a un b,
    aprēķina to kubu summu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    nosakot trīs simbolus aiz komata.

    Argumenti:
        a {int vai float} -- pirmais skaitlis
        b {int vai float} -- otrais skaitlis
    Atgriež:
        int vai float -- argumentu summa
    
    """
    def bilde(a, b):
    bilde=a+b
    return bilde
print("rezultātam 12: ", bilde(-4, -5))
rez=bilde(1,1)
print(rez)
print("pozitīvs + neg tests",bilde(5,-5)==0.0)

"es nesapratu sito"