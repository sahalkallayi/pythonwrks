
number=[5,7,9,10,4,3]

smallest_num=number[-1]

second_smallest=number[0]

for i in number:

    if i< second_smallest and i < smallest_num:

        second_smallest=smallest_num

        smallest_num=i

    elif i<second_smallest and i >smallest_num:

        second_smallest=i

print(second_smallest)