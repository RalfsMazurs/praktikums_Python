""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""

vards = input("Vards:")

if vards!=("Ralfs"):
    print("Uzredzēšanos!")
if vards==("Ralfs"):
    print("Labdien, " + vards + ", pirmdienā!")