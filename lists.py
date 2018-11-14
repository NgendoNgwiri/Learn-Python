#lists of fruits
fruits=['mangoes','passion','pinneaple',"oranges",'apple']
subjects=['biology','chemistry','mathematics','geography']
#[]-lists, 
#{} dictionary
favs_nums = [23,45,67,89,13,78,90,23]#LIST OF INTEGERS
fav_floats =[0.3,0.3,3.7]#list of floating points
favs_letters =['A','B','C','X','Y']# LIST OF CHARACTERS
print(fruits)
print(subjects)
print("---------------------------")
print(favs_nums[4])
print(favs_letters[3])
sum_nums=favs_nums[0]+ favs_nums[6]
print(sum_nums)
temp_in_nairobi =[67,56,77,3,67,88,23,67,80,45,76]
#adding elements to a list
fruits[0]="berries"
fruits[4]="bananas"

fruits.append("strawberry")
fruits.insert(0,"plums")
fruits.insert(12,"lemon")
#delete and pop out elements
print(fruits)
del fruits[4]
fruits.pop()
print(fruits)
print(subjects)
subjects.pop(1)
print(subjects)

#sort and reverse
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

#using a  for loop to create lists
for i in range(0,15):
    print(i)
for fruit in fruits[0:2]:
    print(fruit)