# dividing a code into classes
# class is a blueprints
# class contains variables and methods
# class does not consume memory

class Bank:
  # variables # atributes # properties
  bank_name = ""
  bank_address = ""
  bank_ifsc = 0

# to access class properties we need to create object
# object is instance of class
# object consumes memory
# with the class and object you can organize the logic


b = Bank()   # object creation

b.bank_name = "SBI"
b.bank_address = "Pune"
b.bank_ifsc = 123456

print(b.bank_name)
print(b.bank_address)
print(b.bank_ifsc)

b1 = Bank()

b1.bank_name = "HDFC"
b1.bank_address = "Mumbai"
b1.bank_ifsc = 12345678

print(b1.bank_name)
print(b1.bank_address)
print(b1.bank_ifsc)

b2 = Bank()

b2.bank_name = "ICICI"
b2.bank_address = "Nagpur"
b2.bank_ifsc = 123456789

print(b2.bank_name)
