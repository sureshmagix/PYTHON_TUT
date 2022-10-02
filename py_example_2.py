# This example2 will cover all Data types in python


x=5  #integer
print("Variable type of x is " , type(x))

x=5.5 #float
print("Variable type of x is " , type(x))

x="Hello World"  # String
print("Variable type of x is " , type(x))

x=1j #complex number
print("Variable type of x is " , type(x))

x= ["apple","orange","banana"]  # List 
print("Variable type of x is " , type(x))


x= ("apple","orange","banana") # tuple
print("Variable type of x is " , type(x))

x= range(6) #range
print("Variable type of x is " , type(x))

x= {"apple","orange","banana"}      # set
print("Variable type of x is " , type(x))

x = {"name" : "John", "age" : 36}
print("Variable type of x is " , type(x))
x=frozenset({"apple","orange","banana"}) # frozen set
print("Variable type of x is " , type(x))  

x=True  #bool
print("Variable type of x is " , type(x))  

x=b'hello' #byes
print("Variable type of x is " , type(x))  

x = bytearray(5) #byte array	
print("Variable type of x is " , type(x))  

x=memoryview(bytes(5))
print("Variable type of x is " , type(x))  

x=None
print("Variable type of x is " , type(x))  
