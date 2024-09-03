#print armstrong number

num=int(input("enter number:"))

org=num

total=0

digit_count=len(str(num))

while(num!=0):

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10

print(total)

if(total==org):

    print("armstrong number")

else:

    print("not an armstrong number")
