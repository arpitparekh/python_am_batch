import sys

print(sys.path)
print(sys.version)
print(sys.version_info)
print(sys.platform)

import os  # os module is used for file manipulation

print(os.name)
# os.mkdir("mara_folder")
# os modules gives us file manipulatio methods

for root,dic,files in os.walk("/home/arpit-parekh/Downloads/jar_files"):
  print(dic)


import math

num = 64
print(math.sqrt(num))


# 2^3
n1 = 2
n2 = 3
# **
print(n1**n2)
print(pow(n1,n2))

import datetime as dt

current = dt.datetime.now()
print(current)

# 03 Wed 2024

print(current.strftime("%d %A %B %y %p"))

# file handling
# threading

# try, except # exception handling
# regular expression # regex

# advance python
# json  # advance


num = 12
print("Number is",num)
print(f"Number is {num}")


# break and continue # loop control statement
# break is used to stop the loop

for i in range(1,11):  # jump statement
  if i == 5:
    continue
  print(i)

