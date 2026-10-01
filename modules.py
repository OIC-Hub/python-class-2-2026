# # working with modules
# import math as mth
# from math import sqrt, factorial

# from function import greet
# import random

# print(mth.pi)
# print(sqrt(25))
# print(factorial(5))

# print(greet())

# #working with random
# rand_num = random.randint(000, 999)

# print(rand_num)

# fruits = ["mango", "apple", "orange"]
# sentence = f"I will like to eat {random.choice(fruits)}"

# print(sentence)

# #working with error handling

# try:
#   print(10/2)
# except ZeroDivisionError as e:
#   print(f"An error occured: {e}")

# try:
#   print(20/0)
# except Exception as e:
#   print(f"An error occured: {e}")
  
#working with file
file = open("plain.txt", "r")
print(file.read())
file.close()

file1 = open("test.txt", "w")
file1.write("Python is known for it's simplicity and readability.")
file1.close()

with open("test.txt", "a") as file:
  file.write("\nPython has large community.")

with open("test.txt", "r") as file:
  print(file.read())


import csv
import json

with open("student.csv", "w", newline="") as file:
  content = csv.writer(file)
  content.writerow(["Name", "Age", "Gender", "Height"])
  content.writerow(["Ade", 20, "Male", 4.5])
  content.writerow(["Alice", 17, "Female", 5.5])
  content.writerow(["Samuel", 21, "Male", 4.5])
  content.writerow(["Blessing", 19, "Female", 4.5])
  

person = {
  "name": "Ade",
  "age": 15,
  "gender": "male",
  "height": 5.0,
  "is_active": True
}

with open("person.json", "w") as file:
  json.dump(person, file, indent=2)

with open("person.json", "r") as file:
  print(json.load(file))




