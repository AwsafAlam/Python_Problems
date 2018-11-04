student = {
    'name': 'Awsaf',
    'age': 25,
    'courses': ['Math' , 'Science']
}

print(student['age']) # Prints the value of age. Keys can be strings, or any immutable data type

# e.g
student = {
    1: 'Awsaf',
    'age': 25,
    'courses': ['Math' , 'Science']
}
print(student[1])
## If we try to access a key that is not there, we get key Erroe
# - > defining student a second time also causes this problem

# e.g For print(student['key'])
## But, if we use the get method, not error. This is handled Automatically
print(student.get('phone' , 'not Found'))  ## Returns Not found, if no key is present

student['phone'] = 126317
print(student.get('phone' , 'not Found'))  ## Returns Not found, if no key is present

# We can update values using update method
student.update({1: 'rasid' , 'age': 27})
print(student)

del student[1]
print(student)

## we can also use the pop method
age = student.pop('age')
print(student)
print(age)

print(len(student))  # No. of items in the dict
print(student.keys())
print(student.values())

print(student.items())  # Key value pairs

for key in student:
    print(key) # Loops through the keys

for key , value in student.items():
    print(key , value)