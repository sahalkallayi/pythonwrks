
from re import finditer

text="123wrgd 6$%^"

#pattern="\D" #exclude digits

#pattern="\d" #print digits

#pattern="\w" #[a-zA-Z0-9]

#pattern="\W" #[^a-zA-Z0-9]

#pattern="\s" space

#pattern="\S" exclude space

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())





