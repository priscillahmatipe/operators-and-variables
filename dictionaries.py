# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
school={"name":"mums who code","founder":"Aghama","number of course":"4","course":["data analytics","python programming"]}
#print(school["name"])
#print(school["founder"])
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Dictionary Items
#.item
#print(school.items())
#.get()value 
#print(school.get("name"))
#.keys()all keys  name founder...
#print(school.keys())

#.Value value in dict.items all items and return
#print(school.values())
# Ordered or Unordered

# Changeable, changing items, adding, removing
school["name"]="dads who code"
#print(school)
#adding
school["year founded"]="2020"
#print(school)
#update
school.update({"name":"mums who code"})
#print(school)
school.update({"alumni number":"5000"})
#print(school)
#.pop
school.pop("alumni number")
#print(school)
#.popitem
school.popitem()
#print(school)
#.clear clears everything
# Duplicates Not allowed

# Dictionary Length

# Dictionary Items datatypes

# Type
print(type("thisdict"))
# The dict() constructor

# Copying dictionaries
thisdict={"kitchen":["kettle","blender"],"dinning":["fork","spoon"]}
rooms=thisdict.copy()
#print(thisdict)
#print(rooms)
# Nested dictionaries

# Dictionary Methods
