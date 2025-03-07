import threading
import time

# for multi threaded programming
# theread is a subprocess

def function_one():
  for i in range(1,11):
    time.sleep(1)
    print("Function One:",i)


def function_two():
  for i in range(1,11):
    time.sleep(1)
    print("Function Two:",i)

# function_one()
# function_two()

# we want to run both function at the same time
t1 = threading.Thread(target=function_one)
t2 = threading.Thread(target=function_two)

t1.start()
t1.join()   #doing this in background

t2.start()
