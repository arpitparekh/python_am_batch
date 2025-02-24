class Circle:
  radius = 0

  def area(self):
    print(3.14 * self.radius * self.radius)

  def perimeter(self):
    print(2 * 3.14 * self.radius)

c1 = Circle()
c1.radius = 10
c1.area()
c1.perimeter()

c2 = Circle()
c2.radius = 26
c2.area()
c2.perimeter()

c3 = Circle()
c3.radius = 101
c3.area()
c3.perimeter()
