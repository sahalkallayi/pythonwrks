
from re import fullmatch

gmail_id=input("enter a email id>")

pattern="\\w+@gmail.com"

matcher=fullmatch(pattern,gmail_id)

print("invalid" if matcher==None else "valid")

# + match one or More

# ? optional

# * zero or more

