width	=	input("Give a width: (integer)")
height	=	input("Give a height: (integer)")
result = ""

for i in range(0,height):
	for x in range(0, width):
		result += "*"
	result += "\n"
print result