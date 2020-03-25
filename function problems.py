# 1.
# A bite's strength will affect how long Heibu will scream "awooo!"
# Write a function bite(strength), where strength is a positive number.
# Return or print "awoo" with as many os as the strength of the bite.

def bite(strength):
    return "awo" + strength * "o"
    
print(bite(7))


# 2.
# The City Hall wants to be more friendly with citizens, greeting them
# by their first name, then their last name. However, official records
# store citizens' last name first.
# Write the function greet(lastname, firstname) that will print
# "Good day, firstname lastname!"

# for example,
# greet("Smith", "Jack")
# should print "Good day, Jack Smith"


def greet(lastname, name):
    return "Good day, " + name + " " + lastname

print(greet("Shirado", "Andréa"))


# 3.
# Write a function conjugate(verb) that prints, for example, for "fart",
# I fart
# you fart
# he or she farts
# Assume the verb is a regular one.

def conjugate(verb):
    print("I" + " " + verb)
    print("You" + " " + verb)
    if verb[-1] in ["s", "x", "h", "z"]:
        print("He" + " " + verb + "es")
    else:
        print("He" + " " + verb + "s")

conjugate("write")
conjugate("miss")
conjugate("wash")


# 4.
# Joe hates being called "Joseph". Write a function nickname(name)
# to be installed on Joe's computer so that when he reads email,
# "Joseph" is automatically converted to "Joe".
# If the given name is already "Joe", it should remain "Joe".
# Otherwise, return "I am not [name]".


def nickname(name):
    if name == "Joseph":
        return "Joe"
    elif name == "Joe":
        return "Joe"
    elif name != "Joseph" and name != "Joe":
        return "I'm not" + " " + name
    

print(nickname("Nikita"))
print(nickname("Joe"))
print(nickname("Joseph"))


# 1.
# It's the end of the school year and you need to compile report cards.
# Write a function that says whether a student passes or fails, depending
# on their final exam grade.

# If the grade is 70 points or more (up to 100), the student "Passes".
# Otherwise, the student "Fails"

# Examples:
# report(65) should say "Fails"
# report(92) should say "Passes"

def report(score):
    if score > 69:
        return "Passes"
    else:
        return "Fails"

print(report(65))
print(report(70))
print(report(80))


# 2.
# Key-chan and Heibu just finished a game of Scrabble. Given their scores
# k and h (for Key-chan and Heibu, respectively), report who won the game
# with a function scrabble(k, h)

# If they have the same score, report "Tie"

# Examples:
# scrabble(153, 123) should say "Key-chan"
# scrabble(299, 301) should say "Heibu"
# scrabble(125, 125) should say "Tie"

def results(k, h):
    if k > h:
        return "Key-chan"
    elif k == h:
        return "Tie"
    else:
        return "Heibuu"

print(results(200, 180))
print(results(200, 280))
print(results(200, 200))
















