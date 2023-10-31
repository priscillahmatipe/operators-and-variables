# # A List is a collection which is ordered and changeable. Allows duplicate members.
#fruits = ["pear", "apple", "watermelon", "grape", "cherry", "pineapple"]
#school_info = ["mumswhocode", 4, True, 45.6]
#print(fruits)
#print(school_info)

# # List Items - List items are indexed and you can access them by referring to the index number
# #slicing
# print(fruits[0])
# print(fruits[4])
# print(fruits[0:3])
# print(fruits[5:])
# print(fruits[:3])

# print(fruits[-1])

# print(school_info[-2])

# print(school_info[-4:-1])

# print(fruits[1], fruits[4], fruits[5])
# # Ordered - list items are ordered

# # Changeable, adding and removing - list items can be changed
# fruits[5] = "watermelon"
# print(fruits)

# school_info = ["mumswhocode", 4, True, 45.6]
# # in school_info, replace mumswhocode with mumswhocode.net
# school_info[0] = 'mumswhocode.net'
# print(school_info)

# fruits[0:3] = ["orange"]
# print(fruits)

# # adding
#append method
#fruits.append("watermelon") 
#print(fruits)

# fruits.append("grape")
# print(fruits)

# fruits.insert(-1, "pear")
# print(fruits)

# new_fruits = ["orange", "mango", "grape"]
# fruits.extend(new_fruits)
# print(fruits)

# another_fruits = fruits + new_fruits
# print(another_fruits)


# removing
# .remove
best_friends = ["Nikky", "Florence", "Dee", "Annie", "Blessing", "Sharon", "Samuel"]
#print(best_friends)
#best_friends.remove("Samuel")
#print(best_friends)

# .pop()
best_friends.pop()
print(best_friends)


#best_friends.pop(0)
#print(best_friends)

#best_friends.pop(2) #- valentine
#print(best_friends)

# clear
#list_alphanumeric = [1, "we", 3, 5]
#list_alphanumeric.clear()
#print(list_alphanumeric)

# Allow Duplicates - list allows duplicate items 

# List length
best_friends = ["Nikky", "Florence", "Dee", "Annie", "Blessing", "Sharon", "Samuel"]
# len 
#print(len(best_friends))

# List Items datatypes - list items can have any datatype
list_alphanumeric = [1, "we", 3, 5]
#print(type(list_alphanumeric[0]))

# type()
#print(type(best_friends))

# The list() Constructor
# bag, book, biro, pen
random_list = list(("bag", "book", "biro", "pen"))
#print(random_list)

# Sorting a list
#random_list.sort()
#print(random_list)

random_list.sort(reverse = True)
#print(random_list)

# Copying a list
Stationary = random_list.copy()
#print(Stationary)
#print(random_list)


# Joining a List
# +
new_list = Stationary + random_list
#print(new_list)

#.extend()
sample_list = [1, "they", "them", 5]
new_list.extend(sample_list)
#print(new_list)

# List Methods
# .count()

mytest_score = [16, 17, 9, 15, 12, 12, 17, 12]
#print(mytest_score.count(17))

# .index
#print(mytest_score.index(9))

#.reverse
mytest_score.reverse()
#print(mytest_score)