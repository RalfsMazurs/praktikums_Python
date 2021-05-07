"""
Uzrakstiet programmu Python, 
kas pieņem veselu skaitli (n) un 
aprēķina n + nn + nnn vērtību.
"""
a=input("Ievadi ciparu: ")
aa=str(a)+str(a)
aaa=str(a)+str(a)+str(a)
summa=int(a)+int(aa)+int(aaa)

print(summa)