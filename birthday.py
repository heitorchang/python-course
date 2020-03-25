# birthday

from datetime import date
bday = date(1982, 11, 22)
bday19 = date(2019, 11, 22)
# today = date.today()
today = date(2019, 12, 25)
output = 'keychan is {} years old'
if today < bday19:
    print(output.format(36))
else:
    print(output.format(2019-1982))
