# month calendar for hellokey

from datetime import datetime, date, timedelta
from calendar import monthrange

def caldays(year, month):
    weekslist = []
    first = date(year, month, 1)
    last = date(year, month, monthrange(year, month)[1])
    firstextras = (first.weekday() + 1) % 7
    lastextras = 6 - ((last.weekday() + 1) % 7)

    firstcalday = first - timedelta(days=firstextras)
    lastcalday = last + timedelta(days=lastextras)

    days = (lastcalday - firstcalday).days + 1
    weeks = days // 7
    
    assert firstcalday.weekday() == 6
    assert lastcalday.weekday() == 5

    for i in range(weeks):
        week = []
        for d in range(7):
            week.append({'ymd': datetime.strftime(firstcalday, "%Y-%m-%d"),
                         'label': datetime.strftime(firstcalday, "%d")})
            firstcalday += timedelta(days=1)
        weekslist.append(week[:])
    return weekslist

    # s m t w t f s
    # 6 0 1 2 3 4 5
    # 1 = 6 = 0
    #   1 = 1
    #     1 = 2
    #       1

    # 0 1 2 3 4 5 6
    #     1
    
ans=caldays(2019, 10)
