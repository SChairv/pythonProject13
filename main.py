#Create a function that takes two number strings
# and returns their sum as a string.
def add(x ,y):
    if x == "":
        print("Invalid Operation")
    elif y == "":
        print("invalid Operation")
    else:
        x=int(x)
        y=int(y)
        sumxy=x+y
        sumxy=str(sumxy)
        print(sumxy)
        print(type(sumxy))
x="200"
y="12"
add(x, y )

x=""
y=" 1234"
add(x , y)

x="0"
y=" 250"
add(x,y )