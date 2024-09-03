
#read a number fibinocci or not

number=int(input("enter number:"))

previous=0

current=1

isfibo=False

next=previous+current

while(next<=number):

    next=previous+current

    if(next==number):

        isfibo=True

        break

    previous=current

    current=next

print(isfibo)