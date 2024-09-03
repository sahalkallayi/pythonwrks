#write a program to check palidrome or not

num=int(input("enter number"))

result=0

org=num

while(num!=0):

    digit=num%10

    result=result*10+digit

    num=num//10

print(result)

if(result==org):

    print("palindrome")

else:

    print("not palindrome")
