#Program1
age = int(input("How old are you? "))
if age>=18 :
    print("You are a voter")
else:
    print("You are not a voter")
print()

#Program2
temperature = float(input("Enter current room temperature e.g 23.0: "))
if temperature>25.0:
    print("Hot")

elif temperature<25.0:
    print("Cold")

else:
    print("Normal")
print()

#Program3
num1 =int(input("Enter first number "))
num2 =int(input("Enter second number "))
num3 =int(input("Enter third number "))

if num1>num2 and num1>num3:
    print(num1, "is largest number")

elif num2>num3 and num2>num1:
    print(num2, "is largest number")

else:
    print(num3, "is largest number")




