"""
Uzrakstiet Python programmu, lai iegūtu sfēras
 ar lietotāja norādītu rādiusu tilpumu.
 """

from math import pi
r=float(input("Ievadi skaitli: "))

V= 4.0/3.0*pi* r**3
print("Tilpums ir:",V)