def waterstate(f):
    if f <= 32:
        return"solid"
    elif f >= 212:
        return"gas"
    else:
        return"liquid"

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False

def toGermen(ja,nein):
    if "yes":
        return"ja"
    else:
        return"nein"

def stopLight(c):
    if c == "slow":
        return "green"
    elif c == "slow":
        return "yellow"
    else:
        return "blue"
