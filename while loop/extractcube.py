#sum of cube of each digit

num=int(input("enter a number:"))

total=0

while(num!=0):

    digit=num%10

    exponent=digit**3

    total=total+exponent

    num=num//10

print(total)

