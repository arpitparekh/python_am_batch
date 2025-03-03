# heritance
# varso
# when one class use properties and functions of another class is called inheritance
# with the help of inheritance we can use one class properites and function into another class
# inheritance is used for code reusability

class Person:  # parent class # base class
  name = ""
  age = 0

  def walking(self):
    print("Person is Walking")

class Student(Person):  # inheritance  # child class # derived class
  roll_no = 0

  def studying(self):
    print("Student is Studying")

s = Student()
s.name = "Sumit"
s.age = 10
s.roll_no = 1
s.walking()
s.studying()
