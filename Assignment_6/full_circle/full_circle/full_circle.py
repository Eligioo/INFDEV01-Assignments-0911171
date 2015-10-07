import math
#afstand van de huidige x en y tot het middelpunt is de berekenen met de formule, wanneer de afstand kleiner is dan de radius moet je een asterix printen
user_input = input("Give a size for the circle: (positive integer) ")
radius = user_input/2
result = ""
for x in range(user_input):
    for y in range(user_input):
        distX = (x - radius) * (x - radius)
        distY = (y - radius) * (y - radius)
        distance = math.sqrt(distX + distY)
        if distance < radius:
            #print("("+str(distX)+", "+str(distY)+"), "+str(loc))
            result += "*"
        else:
            result += " "
    result += "\n"
print result