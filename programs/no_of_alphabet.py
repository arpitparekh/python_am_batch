# "Bascom123"

list = ["banana",'apple','orange','grapes','mango']

name = "Bas565656com125656634H56565arsh$$@"

print(len(name))  # used to find the length of  string

alpha_count = 0
digit_count = 0
symbol_count = 0
for i in name:
  if i.isalpha():
    alpha_count = alpha_count + 1
  elif i.isdigit():
    digit_count = digit_count + 1
  else:
    symbol_count = symbol_count + 1

print("Alphabet Count : ",alpha_count)
print("Digit Count : ",digit_count)
print("Symbol Count : ",symbol_count)
