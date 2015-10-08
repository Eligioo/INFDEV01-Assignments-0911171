height = input("Enter an integer for the height: ")
result = ""

for x in range(0, height):
	#formula to calculate amount of stars that must be generated
	generate = (x * 2) + 1
	print generate
	for y in range(1, height - x):
		result += " "
	for z in range(0, generate):
		result += "*"
	result += "\n"
print result