import re

password = raw_input("Choose a password!")
if re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[&'(\-_)=~#{[|`\\^@\]}^$*иг╡%,;:!?./з+]).{6,50}", password):
    strength = "Password is strong!"         
elif re.match('(?=.*[a-z])(?=.*[0-9]).{6,50}', password):
    strength = "Password is medium"
else:
    strength = "Password is weak!"

print strength