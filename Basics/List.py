# data types int, float, bool

array = [1.23, 1.34, 1.53];
# Lists can contain Lists themselves

array2 = [["Awsaf" , 1.34],
        ["sHOMMO", 3.21],
        ["Sadia" , 6.21]
        ]
print(array[2]) # Index
print(array2)

print(array2[1:2]) # Slicing

array[2] = 56;
array2[1:2] = [["New" , 6.42]]
print(array2) # Slicing
# Concat
array2 = array + array2
print(array2)
#del
del(array2[0:3])
print(array2)
