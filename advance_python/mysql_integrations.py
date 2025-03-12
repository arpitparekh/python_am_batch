host = "localhost"
port = 3306
user = "root"
password = "Walden0042$$"
# create database anmg_batch
db = "anmg_batch"

# pip install mysql-connector-python
# Environment

import mysql.connector

def createConnection():
  try:
    db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=db,
    port=port
    )
  except Exception as e:
    print("Error Occured",e)

createConnection()


createTableQuery = "create table if not exists student(id int primary key auto_increment,name varchar(255),age int,gender varchar(10))"

cursor =  db.cursor()
cursor.execute(createTableQuery)
print("Table created successfully")

###################################   insert    #######################
# name = input("Enter Name : ")
# age = int(input("Enter Age : "))
# gender = input("Enter Gender : ")

# insertQuery = f"insert into student(name,age,gender) values ('{name}',{age},'{gender}')"
# cursor.execute(insertQuery)
# db.commit()  # refresh the data in the table
# print("Data inserted successfully")

###################################   update    #######################

# id = int(input("Enter Id : "))
# name = input("Enter Name : ")
# age = int(input("Enter Age : "))

# updateQuery = f"update student set age={age},name='{name}' where id={id}"
# cursor.execute(updateQuery)
# db.commit()  # refresh the data in the table
# print("Data updated successfully")

###################################   delete    #######################
# id = int(input("Enter Id : "))

# deleteQuery = f"delete from student where id={id}"
# cursor.execute(deleteQuery)
# db.commit()  # refresh the data in the table
# print("Data deleted successfully")

###################################   show    #######################
showQuery = "select * from student"
cursor.execute(showQuery)
data = cursor.fetchall()
print(data)
