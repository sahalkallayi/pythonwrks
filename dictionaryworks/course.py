
#update the course as fullstack in students in iteration

# delete a key "place" if it present in the dict using iteration

student={"name":"sahal","course":"datascience","place":"mannarkkad"}

#for i in student:

    #if i=="course":

     #   student[i]="fullstack"

#print(student)

for i in student:

    if i=="place":

        student.pop(i)

print(student)



