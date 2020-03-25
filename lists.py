friends = ["Erik", "Cris", "Giselle", "Daniel", "Claudio"]

acquaintances = ["Vivi", "Gabriel", "Tamara", "Tina", "Feco"]

everybody = friends + acquaintances
everybodies = acquaintances + friends

print(sorted(everybodies))
print(sorted(everybodies, reverse=True))
print(sorted(everybodies, key=len))
print(sorted(sorted(everybodies), key=len))
print(sorted(everybodies, key=lambda n: (len(n), n)))

"""
print(friends[0])
print(friends[-1])
"""


"""
friends.append("Mark")
for friend in friends:
    print(friend.upper())
"""

for index in range(len(friends)):
    if 1 <= index <= 3:
        print(friends[index])


grades = [60, 70, 75, 80, 82, 87, 95]

for grade in grades:
    if grade > 80:
        print(grade)    
        
print(list(range(10)))
print(list(range(10, 16)))
print(list(range(1, 11, 2)))
print(list(range(3, 16, 3)))
print(list(range(5, 0, -1)))
