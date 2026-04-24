print("hello student")

def get_name():
    print("enter your name: ")
    name = input()
    return name

name = get_name()
print("hello " + name)

print("enter your grade: ")
grade = int(input())
print("your grade is " + str(grade))



if grade > 90:
    print("you got an A, you nerd!")
elif grade > 80:
    print("hey man,nice shot")
elif grade > 70:
    print("you passed, barely!")
elif grade < 60:
    print("you failed, you dumbass!")
else:
    print("invalid grade")

print("goodbye")
