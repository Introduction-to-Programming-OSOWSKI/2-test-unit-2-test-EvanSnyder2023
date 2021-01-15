def waterState(f):
    if f <= 32:
        return "solid"
    elif f >= 212:
        return "gas"
    else:
        return "liquid"

print(waterState(50))

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False

def toGermen(t):
    if t == "yes":
        return "ja"
    else:
        return "nein"

print(toGermen("no"))

def stopLight(c):
    if c == "green":
        return "go"
    elif c == "yellow":
        return "slow"
    else:
        return "stop"
