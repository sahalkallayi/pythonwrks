
#find second largest number in list

number=[1,2,3,4,5,7,9,11,10]

largest_num=number[0]

second_largest_num=number[0]

for i in number:

    if i>second_largest_num and i>largest_num:

        second_largest_num=largest_num

        largest_num=i

    elif i >second_largest_num and i<largest_num:

        second_largest_num=i

print(f" second largest number is {second_largest_num}")

# find the sum of odd number

#find the count of odd and even number in the list



