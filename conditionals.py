# Summary/Comparison of Lists, tuples, set, dictionary


# If/ Else/ elif conditions are used to decide to do something based on something being true or false
student_age=12
if student_age < 18:
    print("student is not eligible")

student_age= int(input("what is your age:"))
if student_age < 18:
    print("student is not eligible")    
else:
    print("student is eligible") 

a=int(input("enter a number for a :"))
b=int(input("enter a number for b :"))
#a=b,a<b,a>b
#elseif=elif
if a==b:
    print("the numbers you entered are equal")
elif a>b:
    print("the first number you entered is greater than the second")
else:
    print("the first number you entered is less than the second")
    
#basketball teams,2ft below team a,3ft to 4ft in team b,5ft to 8ft in team c,above 8ft in team d
height=int(input("please enter your heigts in feets"))
if height <2:
    print("you belong to team a")
elif height <=4:
    print("you belong to team b")
elif height <=8:
    print("you belong to team c")
else:
     print("you belong to team d")


        
     
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
age= int(input("please enter your age:"))
threshold=25
if age !=threshold:
    print("persons age is not in threshold")

threshold=[12,25]
if age >=threshold[0] and age <=threshold[1]:
    print("you enter threshold")
else:
    print("you no enter threshold")


# Logical operators (and, or, not) - Used to combine conditional statements




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object




# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
