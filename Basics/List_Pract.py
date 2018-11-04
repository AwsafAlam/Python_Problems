courses = ['Datastructures' , 'AI' , 'Micro' , 'Assembly']

print(courses)
print(courses[0])
print(courses[len(courses) - 1]) # or, we can use negative indexes

print(courses[-1]) ## So, we can traverse in reverse as well

print(courses[0:3]) ## starting at 0 , and upto but not including 3 (ie, < 3 )

print(courses[:2]) # starts at beginning by default
print(courses[1:]) # goes to the end by default 

## (This is lnown as slicing)

courses.append('art')  ## adds at end of list
print(courses)

courses.insert(1 , 'Music') ## adds music at position 1.
print(courses)

nested = ['CSE 322' , 'CSE 221']

courses.extend(nested) ## Adds values from second list to the first at the end 
print(courses)
courses.insert(0 , nested) # creates a list within a list
print(courses)

courses.remove('Datastructures')  ## removes the specified element
print(courses)

popped = courses.pop() # removes the last element. useful when implementing a stack or queue
print(courses ,"Popped -->" ,popped)

courses.reverse() ## reverses our list
print(courses)

nested_list = courses.pop() ## cannot sort nested lists. so, we remove the last element, which is a list
courses.sort() ## sorts in alphabetical order. ## For Numbers, sorts by ascending order
print(courses)

courses.sort(reverse=True) ## sorts in **Reverse**alphabetical order.
print(courses)

sorted_list = sorted(courses) # sorting without changing the original array
print("sorted ->" ,sorted_list)

print(courses.index('art')) # position of element in list
print('art' in courses) # To get a true or false value

for item in courses:
    print(item)

for idx , item in enumerate(courses):
    print(idx, "->" ,item)

print("--------------------------------")
for idx , item in enumerate(courses , start = 2):
    print(idx, "->" ,item)

courses_str = ', '.join(courses) ## turns into a  single comma separated string

print(courses_str)

new_list = courses_str.split(', ')
print("New List =", new_list)

## Lists are mutable (modifiable),
# Tuples are not mutable (not modifyable)

list_1 = ['History' , 'Math' , 'Physics']
list_2 = list_1

list_1[0] = 'Art'

print(list_1)
print(list_2) ## so, values in both lists are changed, since they are referenced

#Immutable
tuple_1 = ('History' , 'Math' , 'Phy')
tuple_2 = tuple_1

# tuple_1[0] = 'Art' -> not possible, since it is immutable. (So, we cannot change a list)

print(tuple_1)
print(tuple_2)
