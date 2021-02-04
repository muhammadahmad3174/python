# global veriable is write outside a function and used inside like..
x = "great"
def myfunc():
    print("teachers are always " + x)

myfunc()
#use inside and outside the function
x = "great"
def myfunc():
    x = "good"
    print("teachers are always " + x)

myfunc()
print("teachers are always " + x)
# global keys
def myfunc():
    global x
    x = "boy"
myfunc()

print("ahmad is a good " + x)


