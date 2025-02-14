# 1234

num = int(input("Enter Number : "))

# 1234//10 = 123
# 123//10 = 12
# 12//10 = 1
# 1//10 = 0

count = 0
while num!=0:
  count = count + 1
  num = num //10

print(count)
