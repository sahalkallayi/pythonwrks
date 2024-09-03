
from re import fullmatch

f=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\regularexpressionwrks\\vehiclereg.txt")

pattern="(KL)( )[0-9]{2}( )[A-Z]{1,2}( )[0-9]{4}"

for line in f:

    vehicle_reg=line.rstrip("\n")

    matcher=fullmatch(pattern,vehicle_reg)

    if matcher !=None:

        print(vehicle_reg)

