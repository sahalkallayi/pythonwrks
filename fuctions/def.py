
def add (n1,n2):

    result=n1+n2

    return result

#print(add(100,300))

def cube(num):

    result=num**3

    return result

#print(cube(5))

def min_two(n1,n2):

    result=n1,n2 if n1<n2 else n2

    return result

#print(min_two(34,78))

def is_odd(num):

    result=True if num%2!=0 else False

    return result

print(is_odd(4))
