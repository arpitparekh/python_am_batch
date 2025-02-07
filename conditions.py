# condition is used to manage the flow of the program

# if else elif

number = 15

if number <10:
  print("Number is greater then 10")
else :
  print("Number is less then 10")


if number!=20 and number<10:
  print("Hi Student")
else:
  print("Hi Teacher")


# greater then 2 numbers

num1 = 200
num2 = 30

if num1>num2:
  print("Num1 is greater then num2")
else:
  print("Num2 is greater then num1")


# check if the number is even or odd

f = 42

if f%2==0:
  print("Even")
else:
  print("Odd")

# check if the number is divisible by 5 and 7

mera_num = 35

if mera_num % 5==0 and mera_num % 7==0:
  print("Divisible by 5 and 7")
else:
  print("Not divisible by 5 and 7")


# elif # multiple condition
# check of the number is positive or negetive or zero

t = 45

if t <0:
  print("Negetive")
elif t>0:
  print("Positive")
else:
  print("Zero")
