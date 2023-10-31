# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
mytuple = (True, "Toyin", 12, "Facilitator")

# Tuple Items - tuple items can be accessed like lists
print(mytuple[2])
print(mytuple[-2])
print(mytuple[0:3])

# Ordered - tuple items are ordered

# Unchangeable or immutable
mylist = list(mytuple)
mylist[0] = False

mytuple = tuple(mylist)
print(mytuple)


# tuples cannot be changed, you can convert a tuple to list to change its content

#unpack a tuple
myfruit_tuple = ("pineapple", "apple", "grape", "avocado", "apple", "strawberry", "blackberry")

# toyin, sarah, rose, priscillah, *chioma = myfruit_tuple

toyin, *sarah, priscillah, chioma = myfruit_tuple
"""print(toyin)
print(sarah)
print(priscillah)
print(chioma)
print(*sarah)
print(sarah[0], sarah[1], sarah[2])"""

# Allow Duplicates
# tuples are indexed so they allow duplicates

# Tuple Length
#print(len(myfruit_tuple))

# Tuple Items datatypes - tuple items can have any datatype
#print(type(mytuple[0]))

# Type()
#print(type(mytuple))

# The tuple() constructor
mylist = ["biro", "book", "pen", "bag"]

mylist_tuple = tuple(mylist)
#print(type(mylist))
#print(type(mylist_tuple))

# Joining tuples
tuple_a = ("chioma", "rose")
tuple_b = ("ijeoma", "sarah")

tuple_c = tuple_a + tuple_b

print(tuple_c)

multi_tuple = tuple_c * 3

#print(multi_tuple)

# multiply tuple


# Tuple Methods

# .count
#.index
