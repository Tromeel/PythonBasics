#A python program that checks whether a number is even or odd
num = int(input("Enter any number: "))
if num ==0:
    print(num, "is neutral")

elif num % 2==0:
    print(num, "is an even number")

else:
    print(num, "is an odd number")
print()


#A python program that checks whether a letter is a vowel or consonant
letter =(input("Enter your letter: "))
if letter =="a" or letter =="e" or letter =="i" or letter =="o":
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")
print()

#A python program that returns a perimeter of a rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
perimeter =(2*(length + width),"is the perimeter of rectangle")
print(perimeter)