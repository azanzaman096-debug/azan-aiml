num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print("The sum of;", num1 + num2)
print("The difference of;", num1 - num2)
print("The product of;", num1 * num2)

if num2 != 0:
    print("The quotient of;", num1 / num2)
else:
    print("Cannot divide by zero.")

print("the greater is:", (num1 > num2))
print("the number or equal is:", (num1 == num2))