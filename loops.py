# loops
# repeatative task
# sequence of instructions repeated

# while
# for

# intital value
# condition
# increment/decrement

# while
val = 10

while val<50:
  print("Hello World")
  val += 1

# print 100 to 1 using while loop in python

val  = 100
while val>0:
  print(val)
  val -= 1


# print all the odd numbers from 1 to 100

val  = 1
while val<=100:

  if val%2!=0:
    print(val)

  val+=1

# for
# range range datatype

for i in range(50,101):  # start,end+1
  print(i)


list = [12,34,56,78,90]
for i in list:
  print(i)


name = "Bascom"

for i in name:
  print(i)


# step size

for i in range(1,11,2):  # start,end+1,step
  print(i)

# 100 -> 1

for i in range(100,0,-1):
  print(i)


# while loop

# val = "a"
# while val<="z":
#   print(val)
#   val += 1
