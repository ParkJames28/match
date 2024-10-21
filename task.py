def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 , num2
def multi(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
    
number1 = int(input("enter a number: "))
number2 = int(input("enter a number: "))
operator = input("select an operator [+,-,*,/]: ")

match operator:
    case "+":
        print(add(number1, number2))
    case "-":
        print(add(number1, number2))
    case "*":
        print(multi(number1, number2))
    case "/":
        print(divide(number1, number2))
    case _:
        print("gg")
