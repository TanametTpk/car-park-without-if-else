import math

def padding(minutes):
    return minutes * 10

def isMoreThanZero(minutes):
    # minutes > 0 ? 1 : 0
    # this function is not working with negative number
    return math.ceil(minutes / (minutes + 1))

def notLessThanZero(minutes):
    moreFactor = minutes / (minutes + 1)
    lessFactor = minutes / abs(minutes + 1)
    # minutes > 0 ? 1 : 0
    # lessFactor + moreFactor For prevent negative number
    return isMoreThanZero(lessFactor + moreFactor)

def isTimeMoreThanZero(minutes):
    # padding for prevent minutes == -1 that cause devide by zero error
    padded = padding(minutes)
    return notLessThanZero(padded)

hours = int(input("enter hours: "))
minutes = int(input("enter minutes: "))

minutes += 60 * hours
cost = 0

# 20 min free
minutes -= 20
minutes += isTimeMoreThanZero(minutes) * 20

# 1 hour 10/hours
cost += isTimeMoreThanZero(minutes) * 10
minutes -= 60

# 2 hour next 20/hours
cost += isTimeMoreThanZero(minutes) * 20
minutes -= 60

cost += isTimeMoreThanZero(minutes) * 20
minutes -= 60

# 3 hour next 40/hours
cost += isTimeMoreThanZero(minutes) * math.ceil(minutes/60) * 40

print(cost)