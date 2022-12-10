from datetime import date
from datetime import time
fdate = date(1998, 12, 12)
print("D.O.B is 12th December 1998")
print("Today is", date.today())
ldate = date.today()
delta = ldate-fdate
print("Number of days lived till now is", delta.days, "days")
