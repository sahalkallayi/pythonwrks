
student={"name":"sahal","course":"python","place":"mannarkkad"}

for i in student:

    if i=="course":

        student[i]="datascience"

for i in student:

    if i =="place":

        new=student.pop(i)

print(new)
