# polymorphism
# poly = many
# morphism = forms


# method polymorphism
# class polymorphism

name = "Bascom"
print(len(name))

list = [1,3,4,65,7,8,9,9]
print(len(list))

# len is polymorph function

def sum(a,b = 10):
  print(a+b)

sum(10)
sum(10,20)   # method overloading

# polymorph function

def add(a,b):
  print(a+b)     # operator overloading

add(1,2)
add("Hello"," Hi")
add([1,2,3],[4,5,6])


# class polymorphism

class Teacher:
  def fun(self):
    print("Teacher is Teaching")

class Student(Teacher):
  def fun(self):
    super().fun()  # calling parent class fun() method into child class

s = Student()
s.fun()
