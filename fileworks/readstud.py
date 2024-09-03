
f=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\fileworks\\students.txt","r")

students=[]

for stud in f:

    students.append(stud.rstrip("\n"))

print(students)