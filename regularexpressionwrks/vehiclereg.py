
from re import fullmatch

vehicle_num=input("enter a vehicle number>")

pattern="[K][L]\d{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")

