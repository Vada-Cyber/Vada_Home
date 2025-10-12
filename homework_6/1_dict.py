students = {
    'name' : 'luka',
    'age' : 23,
    'city' : 'Tbilisi',
    'GPA' : 3.5
}

print (students)

for key, value in students.items():
    print(f"\n{key} : {value}")

    students["city"] = "Gori"
    students["GPA"] = 4.1

students.update({

    'classes' : [ 'Math', 'Physics', 'History'],
    'driver_license' : True,
    'has_car' : False
})

for key, value in students.items():
    print(f"\n{key} : {value}\n")


print (students)

students.pop( "age")
print(students)

del students['GPA']
print(students)