width	=	input("Give integer for the width: ")
height	=	input("Give integer for the height: ")
result	=	""

for x in range(0, height):
	for y in range(0, width):
		if x == 0 or x == (height - 1):
			result += "*"
		else:
			if y == 0 or y == (width -1):
				result += "*"
			else:
				result += " "
	result += "\n"
print result