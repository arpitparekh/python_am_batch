# single level inheritance

class A:
  xyz = 0

class B(A):
  abc = 0


# multi-level inheritance

class P:
  xyz = 0

class Q(P):
  abc = 0

class R(Q):
  num = 0

r = R()
r.xyz = 12
r.abc = 13
r.num = 14

# multiple inheritance

class Parent1:
  a1 = 10
  a2 = 20
  a3 = 30

class Parent2:
  b = 20

class Child(Parent1,Parent2):
  c =30

child = Child()
child.a1 = 12
child.b = 13
child.c = 14

# heirarchical inheritance

# Hybrid Inheritance
class Parent:
  a = 10

class Child1(Parent):
  b = 20

class Child2(Parent):
  c = 30

class Child3(Child2):
  d = 56
