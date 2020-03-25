def doubleprint(text):
    print(text)
    print(text)
doubleprint("byebuu")

def doubleprint(texto):
    print(texto + "y")
    print(texto)
doubleprint("bite")

def doubleprint(texta):
    print(texta + "y" + " " + texta)

doubleprint("shower")

def doubleprint(texta):
    if texta[-1] == "g":
        print(texta + "gy" + " " + texta)
    else:
        print(texta + "y" + " " + texta)
    
doubleprint("pig")
doubleprint("lunch")

def isvowel(letter):
    return letter in "aeiou"
def isconso(letter):
    return letter in "bcdfghjklmnpqrstvxz"

def wordy(word):
    
    if isconso(word[-3]) and isvowel(word[-2]) and isconso(word[-1]):
        print(word + word[-1] + "y" + " " + word)
    else:
        print(word + "y" + " " + word)
