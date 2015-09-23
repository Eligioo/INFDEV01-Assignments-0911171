bValid = False;
while bValid == False:
	celsisus = float(input("Give me the celsisus temp: "))
	if celsisus >= -273.15:
		bValid = True
kelvin = round(celsisus + 273.15, 2)
print(str(kelvin) +" degrees Kelvin")