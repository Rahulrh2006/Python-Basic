#calculator using if elif else 

operator = input("Enter an Operator (+ - / *): ")
num1 = float(input("enter the the 1st number: "))
num2 = float(input("enter the the 2nd number: "))

print(num1 + num2)

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)

else: 

    print(f"{operator} is not a valid operator")