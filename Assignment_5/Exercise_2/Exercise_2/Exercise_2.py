import re

sValue = raw_input("Choose a password!")
if re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[&'(\-_)=~#{[|`\\^@\]}^$*иг╡%,;:!?./з+]).{6,50}", sValue):
    sMessage = "Password is strong!"         
elif re.match('(?=.*[a-z])(?=.*[0-9]).{6,50}', sValue):
    sMessage = "Password is medium"
else:
    sMessage = "Password is weak!"

print sMessage