# A variable is a container for a value, which can be of various types

"""
VARIABLE RULES:
  - A variable name cannot be a reserved keyword
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
  - Can only contain alpha-numeric characters and underscores
"""

# assignning variables
#Toyin="facilitator name"
#toyin="facilitator"
#print=("Toyin")
#Classname1="wednesday 7"
# Assignment Solution
'''write a program that asks for the name of a user, saves it in a variable called name and prints the variable name
HINT: variable name, input(), print()'''


# assigning multiple variables
#name,age,is_female="Pasha",23,True
#print(name)

# Datatypes - int, str, float, bool, list, tuple, set, dictionary
"""int 3
float 22.7
str "3" "Rose"
bool True False"""   #Not kept in quotes because its a boolean value


# Variables can store data of different types, and different types can do different things.
#datatype3=type(3)
#print(datatype3)

# type casting
#new_age=78
#print(type(new_age))
#print(type)(updated_new_age)

#new_name="Rose"
#new_name_new=int(new_name)
#print(type(new_name_new))

#is_female=True
#str_is_female=str(is_female)
#print(str_is_female)
#print(type(str_is_female))


# Strings
#addition=5+6
#print(addition)

"""person1="Layo"
person2="Titi"
print=(person1+person2)
print(person1*3)"""

#sentence="I am a busy bee"
#print(len(sentence))


# assigning strings

# string slicing
"""print(sentence[0]) #result I
print(sentence[4])
print(sentence[:5])"""


# modifying string - uppercase, lowercase, remove whitespace, replace string, split, concatenate, escape characters

#sentence_u=sentence.upper()
#print(sentence_u)

#sentence_l=sentence_u.lower
#print(sentence_l)

#n_persons=",".join([person1,person2])
#print(n_persons)


#Assignment
#Python String Methods
#1.Capitalize Method
#txt = "python,is the best."
#x = txt.capitalize()
#print (x)

#2.Casefold Method
#txt = "Welcome, thankyou for subscribing"
#x = txt.casefold()
#print(x)

#3.Center Method()
#txt = "Grape"
#x = txt.center(20)
#print(x)

#4.count Method()
#txt = "I love apples, apple are my favorite fruit"
#x = txt.count("apple")
#print(x)

#5.encode() Method
#txt = "My name is Ståle"
#x = txt.encode()
#print(x)

#6.endwith() Method
#txt = "Hello, welcome to my world."
#x = txt.endswith(".")
#print(x)

#7.expandstab()Method
#txt = "G\tr\te\ta\tt"
#print(txt)
#print(txt.expandtabs())
#print(txt.expandtabs(2))
#print(txt.expandtabs(4))
#print(txt.expandtabs(10))

#8.find()Method
#txt = "Hello, welcome to my world."
#x = txt.find("welcome")
#print(x)

#9.format()Method
#txt = "For only {price:.2f} dollars!"
#print(txt.format(price = 49))

#10.index()Method
#txt = "Hello, welcome to my world."
#x = txt.index("welcome")
#print(x)

#11.isalnum()Method
#txt = "Company12"
#x = txt.isalnum()
#print(x)

#12.isalpha()Method
#txt = "CompanyX"
#x = txt.isalpha()
#print(x)

#13.isascii()Method
#txt = "Company123"
#x = txt.isascii()
#print(x)

#14.isdecimal()Method
#txt = "1234"
#x = txt.isdecimal()
#print(x)

#15.isdigit()Method
#txt = "50800"
#x = txt.isdigit()
#print(x)

#16.isidentifier()Method
#txt = "Demo"
#x = txt.isidentifier()
#print(x)

#17.islower()Method
#txt = "hello world!"
#x = txt.islower()
#print(x)

#18.isnumeric()Method
#txt = "565543"
#x = txt.isnumeric()
#print(x)

#19.isprintable()Method
#txt = "Hello! Are you #1?"
#x = txt.isprintable()
#print(x)

#20.isspace()Method
#txt = "   "
#x = txt.isspace()
#print(x)

#21.istitle()Method
#txt = "Hello, And Welcome To My World!"
#x = txt.istitle()
#print(x)

#22.isuppper()Method
#txt = "THIS IS NOW!"
#x = txt.isupper()
#print(x)

#23.join()Method
#myTuple = ("John", "Peter", "Vicky")
#x = "#".join(myTuple)
#print(x)

#24.ljust()Method
#txt = "banana"
#x = txt.ljust(20)
#print(x, "is my favorite fruit.")

#25.maketrans()Method
#txt = "Hello Sam!"
#mytable = str.maketrans("S", "P")
#print(txt.translate(mytable))

#26.partition()Method
#txt = "I could eat bananas all day"
#x = txt.partition("bananas")
#print(x)

#27.lower()Method
#txt = "Hello my FRIENDS"
#x = txt.lower()
#print(x)

#28.lstrip()Method
#txt = "     banana     "
#x = txt.lstrip()
#print("of all fruits", x, "is my favorite")

#29.replace()Method
#txt = "I like oranges"
#x = txt.replace("oranges", "berries")
#print(x)

#30.rfind()Method
#txt = "Mi casa, su casa."
#x = txt.rfind("casa")
#print(x)

#31.rindex()Method
#txt = "Mi casa, su casa."
#x = txt.rindex("casa")
#print(x)

#32.rjust()Method
#txt = "banana"
#x = txt.rjust(20)
#print(x, "is my favorite fruit.")

#33.rpartition()Method
#txt = "I could eat bananas all day, bananas are my favorite fruit"
#x = txt.rpartition("bananas")
#print(x)

#34.rsplit()Method
#txt = "apple, banana, cherry"
#x = txt.rsplit(", ")
#print(x)

#35.rstrip()Method
#txt = "     banana     "
#x = txt.rstrip()
#print("of all fruits", x, "is my favorite")

#36.split()Method
#txt = "welcome to the jungle"
#x = txt.split()
#print(x)

#37.splitlines()Method
#txt = "Thank you for the music\nWelcome to the jungle"
#x = txt.splitlines()
#print(x)

#38.startswith()Method
#txt = "Hello, welcome to my world."
#x = txt.startswith("Hello")
#print(x)

#39.strip()Method
#txt = "     banana     "
#x = txt.strip()
#print("of all fruits", x, "is my favorite")

#40.swapcase()Method
#txt = "Hello My Name Is PASHA"
#x = txt.swapcase()
#print(x)
 
#41.title()Method
#txt = "Welcome to my channel"
#x = txt.title()
#print(x)

#42.translate()Method
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
#mydict = {83:  80}
#txt = "Hello Sam!"
#print(txt.translate(mydict))

#43.upper()Method
#txt = "Hello my friends"
#x = txt.upper()
#print(x)

#44.zfill()Method
txt = "50"
x = txt.zfill(10)
print(x)