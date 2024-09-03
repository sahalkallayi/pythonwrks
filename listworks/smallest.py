
#find smallest number in list

number=[1,2,3,4,6,7,0,]

smallest_num=number[0]

for i in number:

    if i<smallest_num:

        smallest_num=i

print(f"smallest number is {smallest_num}")