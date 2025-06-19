#Built-functions/Standard Library Functions
x =max(67,45,68,90,45,43,39)
print("The maximum number is",x)

y = min(67,45,68,90,45,43,39)
print("The minimum number is",y)

z =pow(2,3)
print("The power of 2 is",z)

#User-Defined functions
def greeting():
    print("Hello World!")
greeting() #Calling a function

def school():
    print("My coding school is eMobilis")
school()

#Parameter and Argument
def add(num1,num2):
    print(num1+num2)

add(10,5)
add(14,12)

def student(fullname,course,gender):
    print("My Fullname is",fullname,".","I study",course,". ""My gender is",gender,".")

student("Robin Smith","MIT","Male")

#Python program that displays details of 5 employees Fintech using parameter and argument(Fullname,email,salary,marriage status"
def employee(fullname,age,position,email,salary,marriagestatus):
    print("Fullname:",fullname,"Email:","Age:",age,"Position:",position,"Email:",email,"Salary",float(salary),"Marriage status:",marriagestatus)

employee("Edward Kamau",40,"CEO","Karanja15@gmail.com",200000.00,"Single")
employee("Mercy Wanjiku",31,"Head of Marketing","Mwanjiku23@gmail.com",150000.00,"Single")
employee("Aaron Karanja",27,"Software Engineer","AaronK45@gmail.com",100000.00,"Married")
employee("Joseph Njoroge",34,"Head of Design","Njjoro92@gmail.com",150000.00,"Single")
employee("Emma Nanini",36,"Finance Officer","Nemma922@gmail.com",120000.00,"Married")



