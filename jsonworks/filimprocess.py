
from json import load

f=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\jsonworks\\filim.json")

movies=load(f)

for m in movies:

    print(m.get("title"))

    