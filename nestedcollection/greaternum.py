
arr=[
    [10,20],
    [25,30],
    [40,53]
]

greaternum=[num for lst in arr for num in lst if num>15]

print(greaternum)

