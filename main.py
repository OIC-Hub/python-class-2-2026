# #Number data type
# #interger
# x = 10
# y = 20
# z = 100

# print(x)
# print(type(x))
# print(type(y))
# print(type(z))

# #float
# price = 40.50

# print(price)
# print(type(price))

# #complex
# coordinate = 3 + 4j

# print(coordinate)
# print(type(coordinate))

# #Text data
# #string
# name = "Ade"
# text = 'Python is a good programming language'
# text2 = "I need to go out I'll see you soon"

# num = "200"

# print(name)
# print(type(name))
# print(text)
# print(type(text))
# print(type(num))

# #Boolean data type
# is_active = True
# is_student = False

# print(is_active)
# print(type(is_active))
# print(is_student)
# print(type(is_student))

#Sequential data type
#list
# lst = ["mango", 10, 30.59, True, 3+4j, "orango"]

# print(lst)
# print(type(lst))

# #tuple
# tup = (10)
# tup1 = (10, "mango", "orange", True, 3+4j, 40.78)

# print(type(tup))
# print(type(tup1))

# #set 
# _set = {30, 50, 50, "mango", True, 55, "mango", "orange"}

# print(type(_set))
# print(_set)

# #dictionary
# person = {
#   "name": "Ade",
#   "age": 16,
#   "gender": "Male",
#   "height": 5.5,
#   "is_student": True
# }

# print(person)
# print(type(person))


# #None data
# price = None

# print(price)
# print(type(price))


# #operators
# #arithemetic operators
# num1 = 10
# num2 = 3

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 // num2)
# print(num1 ** num2)

# #comparison
# print(num2 == num1)
# print(num2 != num1)
# print(num2 > num1)
# print(num2 < num1)
# print(num2 >= num1)
# print(num2 <= num1)

#logical 
# print("\nLogical operator")
# print((4 > 2) and (16 < 30))
# print((5 > 20) and (10 > 3))
# print((3 > 1) or (26 > 50))
# print((4 > 15) or (10 > 30))
# print(not (4 > 5))
# print(not (7 < 10))

# #membership
# print("\nMembership operator")
# print("A" in "apple")
# print("a" in "apple")
# print("mango" in ["mango", 20, 30])
# print("W" not in "Watermelon")
# print("Z" not in "orange")

# #tenary operator
# age = 15

# status = "Adult" if age >= 18 else "Child"
# print(status)


# #assignment operator
# x = 3
# y = 2

# x+=y
# print(x)

# x-=y
# print(x)

# x*=y
# print(x)

# x/=y
# print(x)

# x//=y
# print(x)

# x%=y
# print(x)

# x**=y
# print(x)

#working with string
# text = "Python"

# print(text[3])
# print(text[-1])

# text2 = "Python Programming"

# print(text2[0:6])
# print(text2[7:])
# print(text2[:30])
# print(text2[10:3])


# text3 = "   hello world   "

# print(text3)
# print(text3.capitalize())
# print(text3.upper())
# print(text3.strip())
# print(text3.replace("world", "Python"))

# first = "Data"
# second = "Science"

# statement = first + " " + second
# print(statement)

# rep = "Hi " * 3
# print(rep)


# product = "Laptop"
# price = 350

# desp = f"The {product} price is {price}"

# print(desp)

# print(len(product))


#working with string input
# age = input("Enter your age: ")

# sentence = f"You're {age} years old"
# print(sentence)

# print(type(sentence))

# age1 = int(input("Enter your age: "))

# sentence1 = f"You're {age1} years old, you will be {age1 + 1} next year"

# print(sentence1)

#working with list indexing
# fruits = ["mango", "orange", "pipeapple", "watermelon"]

# print(fruits[3])
# print(fruits[-3])

# #list slicing
# print(fruits[1:3])

# fruits.append("cherry")
# fruits.pop(1)
# fruits.insert(2, "apple")
# fruits.remove("cherry")
# print(fruits.index("watermelon"))

# print(fruits)

# #working with tuple 
# color = ("blue", "green", "orange")

# print(color)
# print(color[2])
# print(color[-3])

# print(color.count("green"))
# print(color.index("blue"))

#control structure 1
#conditional statement
# age = 10

# if age >= 18:
#   print("You're an adult.")

# num = 21

# if num % 2 == 0:
#   print("Even number")
# else:
#   print("Odd number")


# score = int(input("Enter your score: "))

# if 70 <= score <= 100:
#   print("Grade A")
# elif 60 <= score <= 69:
#   print("Grade B")
# elif 50 <= score <= 59:
#   print("Grade C")
# elif 40 <= score <= 49:
#   print("Grade D")
# elif 30 <= score <= 39:
#   print("Grade E")
# elif score < 30:
#   print("Grade F")
# else:
#   print("Invalid number")
  
  
# #control structure 2
# counter = 1

# while counter <= 10:
#   print(counter)
#   counter += 1
  
# num1 = 1

# while num1 <= 20:
#   if num1 % 2 == 0:
#     print(num1)
  
#   num1 += 1

# print("End of loop")

# #working with loop
# fruits = ["banana", "orange", "mango", "pawpaw"]

# for fruit in fruits:
#   print(fruit)

# text = "PYTHON"

# for char in text:
#   print(char)
  
# for num in range(8):
#   print(num)
  
# square = [x**2 for x in range(12)]

# print(square)


#working with dict object mapping
student = {
  "name": "Alice",
  "age": 20,
  "gender": "female",
  "height": 6.5,
  "is_active": True
}

print(student)
print(student["name"])


car = {
  "name": ["Camry", "Accura", "GLK"],
  "year": [2022, 2015, 2023],
  "make": ["Toyota", "Honda", "Mercedes-Benz"],
  "transimission": ["Automatic", "Manuel", "Automatic"]
}

print(car["name"][2])


#CRUD operation
person = {}

print(person)

#create operation
person["name"] = ["Ade", "John", "Samuel"]
person["age"] = [18, 16, 17]
person["gender"] = ["Male", "Male", "Male"]

#retrieve operation
print(person["name"][1])
print(person["age"][2])
print(person["gender"])

#update operation
person["age"][0] = 20
person["name"][2] = "Samuel Adeyemi"

#delete operation
del person["age"][2]
person.pop("name")

print(person)


