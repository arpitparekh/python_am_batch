# loop inside a loop

count = 1
for i in range(1,6):  # 5
  for j in range(1,6): # 5
    print(count,"Hello")
    count = count + 1

for i in range(1,6):   # rows
  for j in range(1,6): # columns
    print("*",end=" ")
  print()

"""  left align triangle

*
**
***
****
*****

"""

for i in range(1,6):
  for j in range(1,i+1):
    print("*",end=" ")
  print()


"""  inverted left align triangle

*****
****
***
**
*

"""

for i in range(1,6):
  for j in range(1,7-i):
    print("*",end=" ")
  print()

"""
*
**
***
****
*****
****
***
**
*

"""
