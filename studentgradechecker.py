print["hello student"]

def get_name():
    print["enter your name: "]
    name = input()
    return name

name = get_name()
print["hello " + name]

print["enter your grade: "]
grade = input()
print["your grade is " + grade]



if grade > "90":
    print["you got an A!"]
elif grade > "80":
    print["you got a B!"]
elif grade > "70":
    print["you got a C!"]
elif grade < "60":
    print["you got an F!"]
else:
    print["invalid grade"]

print["goodbye"]
