#1
from datetime import date 
today = date.today()
a = today.day - 5
res = date(today.year,today.month,a)
print(res)

#2
from datetime import date 
from datetime import timedelta
today = date.today()
yest = today - timedelta(days = 1)
tom = today + timedelta(days = 1)
print(yest,today,tom)

#3
from datetime import datetime 
now = datetime.now()
a = now.replace(microsecond = 0)
print(a)

#4
from datetime import datetime
def sec(now,not_now):
    res = now - not_now
    return int(res.total_seconds())
now = datetime.now()
not_now = datetime.strptime("2020-12-26 02:00:07","%Y-%m-%d %H:%M:%S")
print(sec(now,not_now))