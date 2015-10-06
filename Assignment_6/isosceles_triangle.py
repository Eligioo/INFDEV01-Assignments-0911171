height = input("Enter an integer for the height: ")
result = ""

for x in range(0, height):
	for y in range(0, height):
		result += "*"
	result += "\n"
print result