#working with function
def greet():
  print("Hello, Welcome to Python.")

greet()

def greeting():
  name = "Alice"
  return f"Hello {name}"

print(greeting())

def add_number(num1, num2):
  result = num1 + num2
  return result

print(add_number(10, 20))

#working with simple calculator
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def division(a, b):
  if b == 0:
    return "You can't divide by 0"
  else:
    return a / b

def multiply(a, b):
  return a * b

def main():
  while True:
    print("\n/---------Simple Calculator------------/")
    print("1. For Addition")
    print("2. For Subtraction")
    print("3. For Multiplication")
    print("4. For Division")
    print("5. Type 'q' to exit the program")
    
    choice = input("Enter your calculation choice: ").strip()
    
    if choice in ['1', '2', '3', '4']:
      num1 = float(input("Enter your first number: ").strip())
      num2 = float(input("Enter your second number: ").strip())
      
    if choice == "1":
      print(f"Addition for '{num1}' and '{num2}' is: {add(num1, num2)}")
      
    elif choice == "2":
      print(f"Subtraction for '{num1}' and '{num2}' is: {subtract(num1, num2)}")
    
    elif choice == "3":
      print(f"Multiplication for '{num1}' and '{num2}' is: {multiply(num1, num2)}")
      
    elif choice == "4":
      print(f"Division for '{num1}' and '{num2}' is: {division(num1, num2)}")
    
    elif  choice == "q":
      print("Good bye!")
      break
    
    else:
      print("Invalid choice")

if __name__ == "__main__":
  main()