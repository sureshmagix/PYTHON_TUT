from tkinter import E


print("hi this a test message AB")

x=7;y="ABC";
print(x);
print(y)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

a=6;b=7;
print(a+b)  #output vaiable


e = "awesome"

def myfunc():
  e="TEST"   #local variable
  print("Python is " + e) #printing local variable

myfunc()
print(e) # printing global variable

