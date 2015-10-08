height = input("Enter an integer for the height: ")
result = ""

for x in range(0, height):
	stars = (x * 2) + 1
	for y in range(1, height - x):
		result += "-"
	for z in range(0, stars):
		result += "*"
	result += "\n"
print result