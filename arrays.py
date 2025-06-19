
courses = ["Fullstack", "Data Science", "CyberSecurity"]
print(courses)

#Accsessing an element
print(courses[2])

#Looping through an array
for course in courses:
    print(course)

#Adding new element
courses.append("UI/UX")
print(courses)

#Removing an element
courses.remove("Data Science")
print(courses)
