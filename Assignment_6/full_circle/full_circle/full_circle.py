import math
user_input = input("Give a size for the circle: (positive integer) ")
radius = user_input/2
result = ""
for x in range(user_input):
    for y in range(user_input):
        DistX = x - radius
        DistY = y - radius
        Dist = math.sqrt((DistY**2) + (DistX**2))
        if Dist < radius:
            result += "*"
        else:
            result += " "
    result += "\n"
print result