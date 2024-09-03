#swap odd numbers in another list

num=[2,3,4,5,6,7,89]

odd_num=[]

for i in num:

    if i %2!=0:

        odd_num.append(i)

print(odd_num)