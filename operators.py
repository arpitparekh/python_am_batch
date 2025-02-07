# operators are the symbols used to perform operations on variables and values
# 1. Arithmetic operators
# + - * / // % **

n1 = 10
n2  = 20
n3 = n1 + n2
print(n1+n2)
# print(10+20)
print(n1-n2)
print(n1*n2)
print(n1/n2)  # float

num1 = 40
num2 = 10
print(num1/num2)

# integer division
# //

print(num1//num2)

k = 40
j = 45
print(k//j)

# % (modulus / modulo)  # reminder
q = 20
w = 12

print(q % w)

print(1234 % 10)   # 4
print(1234 // 10)  # 123

# ** (exponent)
print(10 ** 101)

# relational operators
# < > <= >= == !=
# relational operator always gives boolean value

v1 = 10
v2 = 20
v3 = v1<v2

print(v3)
print(type(v3))
print(v1<v2)
print(v1>v2)
print(v1<=v2)
print(v1>=v2)
print(v1==v2)  # equality operator
print(v1!=v2)

# logical operators
# and or not  # boolean values

val1 = 10
val2 = 20

print()

# and
print(val1!=val2 and val1<val2)

height = 123.45
age = 45

# or
print(height>120 or age<40 or val1<val2 or val1!=val2)


# not
print(not(val1<val2))

# assignment operators # use to assign values to variables
# = +=  -= *= /= //= %= **=

a = 6

a **= 2

print(a)
