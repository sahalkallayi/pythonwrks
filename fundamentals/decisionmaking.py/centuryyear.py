#print century year if year ends with two zero

year=int(input("enter year:"))

if year %100==0:

    print(f"{year}century year")

else:

    print(f"{year}non century year")