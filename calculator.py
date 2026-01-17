#add,subtract,multiply,divide
#handle division by zero
#use only numbers as input
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: Division by zero"
    return a/b

while True:
    print("New Calculation")
    print("enter first number:")  
    num1=int(input())
    print("enter second number:")
    num2=int(input())
    print("Addition of numbers:",add(num1,num2))
    print("Subtraction of numbers:",subtract(num1,num2))
    print("Multiplication of numbers:",multiply(num1,num2))
    print("Division of numbers:",divide(num1,num2))
    print("Do you want to continue? (y/n)")
    choice=input()
    if choice=='y':
       continue
    else:
           break
        
