#write a program to read student name and 3 marks mark1,mark2,mark3
#and print total mark and average mark

stud_name=input("enter student name:>")

mark1=input("enter mark1:>")

mark2=input("enter mark2:>")

mark3=input("enter mark3:>")

total=int(mark1)+int(mark2)+int(mark3)

avg=total/3

print(f"student name{stud_name} total mark{total} avg={avg}")
