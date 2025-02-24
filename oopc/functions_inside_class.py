class Vehicle:
  model = ""
  color = ""
  price = 0

  # wheever you create a function inside a class it will always have self parameter
  # self is a its own class object inside that class

  def running(self):
    print(self.model)
    print(self.color)
    print(self.price)
    print("Vehicle is Running")

  def dancing(self,a,b):
    print(a+b)
    print("Vehicle is Dancing")

v = Vehicle()
v.model = "Honda City"
v.color = "Black"
v.price = 1200000

v.running()
v.dancing(10,20)

v1 = Vehicle()
v1.model = "BMW"
v1.color = "White"
v1.price = 12000000

v1.running()
