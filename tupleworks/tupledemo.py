
# tuple

#define by()

#tuple ()    index positioning , duplicates allow , immutable

#=================================================================

# set

name={"hari","sukumar","hello","hello"}

print(name)

#s=set()

#print(type(s))

#duplicates not allowed
#elements are unorder
# cannot use index positioning
#mutable

#=====================================================================


numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]

new_num=list(num)

new_num.append(500)

numbers[2][1]=tuple(new_num)

#print(numbers)

                
                      