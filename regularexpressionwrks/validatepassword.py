
# 1st char uppercase alpha
# next char digit 1-9
# next digit 0-9
# 4th place 0 or 1 space
# next 4 char any number from 0-9
# last char 1-9

from re import fullmatch

passportid=input("enter a passport id>")

pattern="[A-Z][1-9][0-9][0| ][0-9]{4}[1-9]"

matcher=fullmatch(pattern,passportid)

print("invalid" if matcher==None else "valid")








