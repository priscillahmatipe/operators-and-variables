# A Set is a collection which is unordered and unindexed. No duplicate members.
myset={"Rose","Chioma","Joy","Priscillah","Sarah","Ijeoma"}
#print(myset)
#print(myset)
# Set Items.... Checks if a value is true/false
#student_name="Rose"
#print(student_name in myset)

# Unordered

# Unchangeable
#.add()
myset.add("Toyin")
#print(myset)
myset.add("Toyin")
#print(myset)
#.update()
invite=["Bolaji","Lucy","Ayonikun is a boy"]
myset.update(invite)
#print(myset)
#.remove
myset.remove("Ayonikun is a boy")
#print(myset)
#.pop Removes random item
myset.pop()
#print(myset)
#.discard
myset.discard("Toyin")
print(myset)
#.clear deletes everything
myset.clear()
#print(myset)
# Duplicates not Allowed

# Getting the length of a set
#write a program to print the length of invite
invite=(set(invite))
#print(len(invite))
#.union
# Sets Items datatypes
# Type
#print(type(invite))
# The set() constructor

# Joining sets
#.update
myset=("Chioma","Rose","Ijeoma")
#print(myset)
#myset.update(invite)
#print(myset)
#union
new_participants=("Toyin","Sarah")
#mynewset=myset.union(new_participants)
#print(mynewset)
#Intersection
kitchen_app={"pot","kettle","blender","spoon","cutlury"}
dining_app={"kettle","spoon","cutlury","table","basin"}
kitchen_dining_intersect=kitchen_app.intersection(dining_app)
print(kitchen_dining_intersect)


#study five other set methods