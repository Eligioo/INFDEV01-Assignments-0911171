import math
sAsterisks = ""
iNumber = 10
iRadius = iNumber/2
for i in range (0, iNumber+2):
    for o in range (0, iNumber):
        iYdist = abs(i - iRadius)
        iXdist = abs(o - iRadius)
        if int(math.ceil(math.sqrt(iYdist**2 + iXdist**2))) < iRadius:
            sAsterisks += "*"
        else:
            sAsterisks += " "
    sAsterisks += "\n"

print sAsterisks