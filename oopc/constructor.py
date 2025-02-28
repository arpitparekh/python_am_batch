# constrctor in python
# constrcutor is special method that calls automatically and use to intialize the variables
# in python constrcutor is called __init__()
# constrcutor is used to intialize the variables and create an object
# everyclass only have one constrcutor

class MyClass:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c


mc = MyClass(1,2,3)
print(mc.a)
print(mc.b)
print(mc.c)

class Circle:
  def __init__(self,radius):
    self.radius = radius

  def area(self):
    print(3.14 * self.radius * self.radius)

c = Circle(10)
c.area()

# class
# object
# constructor

# inheritance
# polymorphism

# abstraction
# encapsulation


class MeghnaStudent:


  def __init__(self,age,height):
    self.age = age
    self.height = height

  def dance(self):
    print("Meghna is Dancing")

m = MeghnaStudent(23,5.5)
print(m.age)
print(m.height)


# tomorrow

# inheritance
# polymorphism
