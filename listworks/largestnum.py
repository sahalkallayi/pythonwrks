
#find largest number in list without using methods

number=[2,4,6,8,13,123]

largest_num=number[0]

for i in number:

    if i>largest_num:

        largest_num=i

print(f"largest number is {largest_num}")
