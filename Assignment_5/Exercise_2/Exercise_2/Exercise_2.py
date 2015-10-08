password = raw_input("Choose a password \n")
password_length = len(password)
result = ""

upperChars      = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerChars      = "abcdefghijklmnopqrstuvwxyz"
digitChars      = "0123456789"
specialChars    = "!@#$%^&*()-_=+[]{};:'<>,./?"

lowerCount = 0
upperCount = 0
digitCount = 0
specialCount = 0

for char in password: 
    if char in upperChars:
        upperCount = upperCount + 1
    elif char in digitChars:
        digitCount = digitCount + 1
    elif char in specialChars:
        specialCount = specialCount + 1
    elif char in lowerChars:
        lowerCount = lowerCount + 1

if specialCount > 0 and digitCount > 1 and upperCount > 1 and lowerCount > 1:
    result = "Password is strong"
elif digitCount > 1 and upperCount > 1 and lowerCount > 1:
    result = "Password is medium"
elif password_length < 6:
    result = "Password is to short."
else:
    result = "Password is weak"

print result