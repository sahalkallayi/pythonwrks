
#swap to remove even numbers from the list

num=[1,2,3,4,5,6,7,8,9]

for i in num:

    if i%2==0:

        num.remove(i)

print(num)

