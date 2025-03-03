# inheritance with constructor
# golden rule of inheritance with constructor
# when there is a constrcutor in parent class we must have to call that constrcutor inside a child class constrcutor explicitly

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name)
    print(self.age)

class Student(Person):
  def __init__(self, roll_no,name,age):
    super().__init__(name,age)  # super()
    # we must have to call parent class constrcutor into class class constrcutor
    self.roll_no = roll_no


s = Student(12,"Sumit",23)
s.display()

s1 = Student(13,"Amit",25)
s1.display()
