height = input("Give the max height of the triangle: ")
counter = 1
result = ""

for x in range(0, height):
	for x in range(0, counter):
		result += "*"
	result += "\n"
	counter = counter + 1

print result