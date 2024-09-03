
expenses=["10000","15000","17000","19000","25000","38000"]

#find count

expense_count=len(expenses)

#print(expense_count)

#print all expenses

#for i in range(0,len(expenses)):

    #print(expenses[i])

#print<15000

#for i in range(0,len(expenses)):

    #if expenses[i] > 15000:

        #print(expenses[i])

#print total expense

total_expense=0

for i in range(0,len(expenses)):

    total_expense=total_expense+expenses[i]

print(total_expense)