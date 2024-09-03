
from re import finditer

text="acvlm,2345 )*@#ASDacLKJH"

#pattern="[ac]" chk for either a or c

#pattern="[a-o]" chk for alphabets a to o

#pattern="[a-z]"

#pattern="[A-Z]"

#write a pattern for matching all alphabets

#pattern="[A-Za-z]" chk all alphabets

#pattern="[0-9]" chk for digits

#pattern="[A-Za-z0-9]" chk for alphanumeric characters

#pattern="[^A-Za-z0-9\s]"

#pattern="[\s]"


matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())

