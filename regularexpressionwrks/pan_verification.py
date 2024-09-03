
# first 3 char are alpha

# 4th place PCAFHT

# 5th place alpha

# 4 digit

# 1 alpha


from re import fullmatch

pan_number=input("enter the pancard number>")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,pan_number)

print("invalid" if matcher==None else "valid")

