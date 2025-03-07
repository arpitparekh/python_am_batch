# exception (solvable abnormality in the code)
# error

num = 12

try:
  print(num/0)
except:
  print("Error Occured")

print("Rest of the code")

name = "123"
try:
  print(int(name))
except:
  print("Error Occured")
else:
  print("No Error")
finally:
  print("This is Finally block")  # this block will execute in every case # cleanup

number = int(input("Enter a number : "))
print(number)

list = [12,34,56,78,90]
# print(list[100])
