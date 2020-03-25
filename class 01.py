print("Hello, world!")

print(7*8)

print("7*8")

print(print)

print("1" + "3")

name = "Heibu"

print(name)
print(name + " " + name)

for i in range(10):
    print(name + "_", end="")

print("Key-chan right!")

for i in range(9):
    print(name + "_", end="" + name)

name = "Heibu "
name2 = "Heibu"

print(name * 9 + name2)

print("7" * 8)


# birthday

import datetime

birthday = datetime.date(1982, 11, 22)
today = datetime.date.today()
bday2020 = datetime.date(2020, 11, 22)
future = datetime.date(2022, 3, 20)

print(birthday)
print(datetime.date.today())
print(datetime.date.today)

print(today - birthday)
print(today.year)
print(today.year - birthday.year)

if today < bday2020:
    print(today.year - birthday.year - 1)

print(future.year - birthday.year)
