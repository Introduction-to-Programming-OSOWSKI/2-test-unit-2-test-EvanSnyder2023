def waterstate(f):
    if f <= 32:
        return "solid"
    elif f >= 212:
        return "gas"
    else:
        return "liquid"

def isDozen(d):
    if d % 12 == 12:
        return True
    else:
        return False

def toGermen(ja,nein):
    if True:
        return ja
    else:
        return nein

def stopLight(c):
    if c == "slow":
        return "green"
    elif c == "slow":
        return "yellow"
    else:
        return "blue"
