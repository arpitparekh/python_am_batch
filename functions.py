# functions
# function is a block of code that runs when we called
# functions improve code reusability and readability
# def

# function name
# function body
# function parameter
# function return type

def mara_function():
  print("Hello World")
  print("Hello Student")
  print("Hello Teacher")

mara_function()  # function calling
mara_function()  # function calling
mara_function()  # function calling
mara_function()  # function calling

# function with parameter

def greeting(name):   # name is parameter
  print("Hello",name)

greeting("Raj")
greeting("Ravi")
greeting("Ramesh")
greeting("Rajesh")


def sum(a,b):
  print(a+b)

sum(10,20)
sum(100,200)
sum(1000,2000)

######################################################

# function with return type

def sabka_function():
  return 34

# when function return something, whole function becomes the retunring value

print(sabka_function())

result = 10 + sabka_function()
print(result)

# function with parameter and with return type

def sum(a,b):
  return a+b

print(sum(10,20))
print(sum(100,200))
print(sum(1000,2000))

def sub(a,b):
  return a-b

print(sub(100,20))

print( sum(  sub( sum (10,20),20)  , sub(80,20)  ) )   # function inside a another function parameter

# higher order function

def left_align_triangle(n):
  for i in range(1,n):
    for j in range(1,i+1):
      print("*",end=" ")
    print()


# left_align_triangle(12)
# left_align_triangle(int(input("Enter Number : ")))
# left_align_triangle(int(input("Enter Number : ")))

# function with parameter args and kwrags

def display_karo(*args):
  print(args)  # tuple


display_karo(2,3,"Hello",324,4545.45,True)

# keyword arguments

def mera_function(name,phone,address):
  print(name)
  print(phone)
  print(address)


# mera_function("Raj",8978978978,"Pune")
# if you want to mantain the parameter order then you can use keyword arguments
mera_function(address="Pune",name="Raj",phone=8978978978)

# kwargs

def mera_function(**kwargs):  # dictionary
  for i in kwargs:
    print(i,kwargs[i])


mera_function(age = 23,address = "Pune",phone = 8978978978,name = "Raj",salary = 234234234234)

# default argument
def sum_karo(a,b,c=20):
  return a+b+c

print(sum_karo(10,20))

# lambda function
# function without any name
# lambda function is a anonymous function
# lambda function is a one liner function

demo = lambda name : print(name)

# def demo(name):
#   print(name)

demo("Raj")

# veriables
# datatypes
# operators
# conditional statements
# loops
# loop inside loop # patterns
# functions
# lambda function

# oopc # object oriented programming concepts
