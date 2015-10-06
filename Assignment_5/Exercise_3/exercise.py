#ord -> return number
#chr -> return letter
textInput   = raw_input("What string has to be shifted? ")
intShift    = input("How many steps do I need to shift? ")
textTotal   = ""

for letter in textInput:
    if letter.isalpha():
        cypher = ord(letter) + intShift
        if letter.islower():
            if cypher > ord("z"):
                cypher -= 26
            elif cypher < ord("a"):
                cypher +=  26
        else:
            if cypher > ord("Z"):
                cypher -= 26
            elif cypher < ord("A"):
                cypher += 26
        textTotal += chr(cypher)
    else:
        textTotal += letter
print textTotal