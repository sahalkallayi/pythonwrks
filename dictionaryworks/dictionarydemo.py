
# dict={key:value}

# key should be unique 
#=======================
student={"name":"sahal","course":"python"}

#print(student["name"])

student["name"]="hari"

#print(student)

student['place']="chennai"

#print(student)

new=student.items()

#print(new)

for i in student:

    print(f"{i}={student[i]}")

