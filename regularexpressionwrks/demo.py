
from re import finditer

text="hellopythonhellopythonhellopython"

matcher=finditer("hello",text)

count=0

for m in matcher:


    print(m.start(),"===",m.group())

    count+=1

print("total count" ,count)




    

    

