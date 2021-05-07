"""
Izveidot funkciju, kura atgriež skaitļu kvadrātus, lietotāja norādītā apgabalā.
"""

def kvadratus(x):
    return x * x

print(list(map(kvadratus, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))