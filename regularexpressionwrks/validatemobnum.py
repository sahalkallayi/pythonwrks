
from re import fullmatch

mob_num=input("enter a mobile number>")

pattern="(91)\\s?[6-9]\\d{9}"

matcher=fullmatch(pattern,mob_num)

print("invalid" if matcher==None else "valid")
