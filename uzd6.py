"""
Uzrakstiet programmu Python,
lai aprēķinātu dienu skaitu starp diviem datumiem.
"""

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 9, 11)
delta = l_date - f_date
print(delta.days)