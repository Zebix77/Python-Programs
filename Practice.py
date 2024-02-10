
# Write a script that initializes 2 variables n1 and n2 with the values 8 and 9 (accordingly).

# After that initialize another variable n3 that will hold whether n1 is bigger than n2.
# SOLUTION:
# n1=8
# n2=9
# n3=n1!=n2
# print(n3) = True


# b=12
# a=2
# c=(12*2)
# print(c)

# a=20
# b=20
# print(a+b)
  
# length=9
# width=13
# area_of_rectangular=(length*width)
# print(area_of_rectangular)

# num1= int(input("Enter the first number:"))
# num2= int(input("Enter second number"))
# sum=(num1+num2)
# print("Sum of numbers:" , sum)

# num=int(input("Enter the number:"))
# if num %2==0:
#     print("EVEN NUMBER")
# else: print("ODD NUMBER")

# VALUE SWAPPING:
# a=20
# b=90
# print("Before swapping: a=", a, "b=",b)
# a,b=b,a
# print("After swapping:a=",a, "b=",b)
#  Before swapping: a= 20 b= 90
# After swapping:a= 90 b= 20

# TYPE CASTING 
# a=float("5")
# b=10
# print(a+b) = 15.0

# a = int(input("Enter the number1"))
# b = int(input("Enter the number 2"))
# print(a+b)

# l = 4
# w= 4
# print("AREA:",l*w ) 

# a=eval(input("Enter the number 1:"))
# b=eval(input("Enter the number 2:"))
# print(("Average:"), (a+b)/2)

# a=int(input("ENTER THE VALUE:"))
# b=int(input("ENTER THE VALUE:"))
# print(a>=b)

# ENDSWITH FUNCTION:
# str1="I am studying python on Apna College"
# print(str1.endswith("ege"))
# ENDSWITH CHECKS IF STRING ENDS WITH GIVEN STRING
 
# REPLACE FUNTION IS USE TO REPLACE STRING WITH ANOTHER STRING
# str="I am studying python on Apna College"
# print(str.replace("o","a"))
# OUTPUT="I am studying pythan an Apna Callege"

# x = input("Enter your first name:")
# print(len(x))

# str="I have 25$ in my bank account"
# print("RESULT OF YOUR FIND FUNCTION IS:", str.count("$"))


# x = int(input("ENTER THE NUMBER:"))
# if x % 2==0:
#     print("EVEN NUMBER")
# else: print("ODD NUMBER")

# a = int(input("ENTER FIRST NUMBER:"))
# b = int(input("ENTER SECOND NUMBER:"))
# c = int(input("ENTER THIRD NUMBER:"))
# if a>=b and a>=c:
#     print("A IS THE GREATEST")
# elif b>=a and b>=c:
#     print("B IS THE GREATEST")
# elif c>=a and c>=b:
#     print("C IS THE GREATEST")


# x = int(input("Enter the number:"))
# if x %7==0:
#     print(True)
# else: print(False)

# l=[100]
# l.extend([10,20,30,50])
# print(l)

# ADD/APPEND,EXTEND VALUES INTO LIST ALSO SORTING VALUES IN REVERSE IS DOWN BELOW:
# list=[7,10,28,34,67,3,5,9,87,112]
# list.extend([90,100,25,89,1000,988,677])
# list.sort(reverse=True)
# print(list)

# INSERT VALUE IN FUNCTIONS:
# list=[10,20,30,40,50]
# list.insert(2,95)
# print(list)

# value = []
# print(value)
# print(type(value))

# x1 = input("ENTER YOUR FIRT FAV MOVIE NAME:")
# x2 = input("ENTER YOUR SECOND FAV MOVIE NAME:")
# x3 = input("ENTER YOUR THIRD FAV MOVIE NAME:")
# list=[]
# list.extend([x1,x2,x3])
# print(list)


# x=[1,2,3]
# copy_list=x.copy()
# copy_list.reverse()
# if copy_list==x:
#     print("PALINDROME")
# else: print("NOT PALINDROME")

# grade = ("A", "B", "C", "D", "E" "F", "A", "A",)
# print(grade.count("B"))

# list = ["K", "B", "G", "Z", "L", "F",]
# list.sort()
# print(list)

# DICTIONARIES:
# info = {"country" : "pakistan",
#         "age" : "19",
#         "city" : "Islamabad",
#         "village" : "harnal",
#         "name" : "shahzaib ali",}
# print(info ["village"])


# SET DATA TYPE:
# SETS = {1,2,3,3,4,7,7,7, "Hello world", "srring"}
# print(SETS)
# print(type(SETS))
# SET IGNORE DOUBLE VALUES AND IS & UNORDERED. SET IS MUTABLE BUT IT'S ELEMENTS ARE IMMUTABLE (CANNOT BE CHANGED)
#set() is the way to write an empty set


# x=set()
# x.add(1)
# x.remove(1)
# print(x)
 

# dict = {"Car" : "Bugatti Chiron ",
#         "Bike": "Kawasaki Ninja H2R",
#         "Fav SUV" : "Range Rover",
#         "Aimal" : "Cat"
#         }
# print(type(dict))
# print(dict)

# classes  = {"Python", "Java", "C++", "C++", "Javascript", "C++", "Pyhton", "Java"}
# print(len(classes))


# a = int(input("pyshic marks:"))
# b = int(input("math marks:"))
# c = int(input("english marks:"))
# dict = {}
# dict.update({"physics:" : a})
# dict.update({"math:" : b})
# dict.update({"english:" : c})
# print(dict)


# WHILE LOOP:
# i = 2
# while(i<=11):  
#     print(i)
#     i = i + 2 

# a = int(input("Enter the number:"))
# while(True):
#   if a%2 == 0:
#     print(a)

# def GreetHello(): 
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello") 
# print("Executing the function")
# GreetHello() 
# print("Done")
# print("function is finished")

# loop = 100 #Starting point
# while loop >= 1: #Stopping point
#     print(loop) #What yu want to print
#     loop -= 1 #Increment or Decrement
    
# i = 3
# while i <= 30:
#     print(i)
#     i += 3

# i = 1
# while i<=10:
#     print(i*3)
#     i += 1


# i = [10,20,30,40,50,60,70,80,90,100]
# idx = 0
# while idx < len(i):
#     print(i[idx])
#     idx+=1

# nums = (10,20,30,40,50,60,70,80,90,100)
# x= 50
# i=0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found at idx" , i)
#     i +=1


# nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# x = 50
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("Found at idx", i)
#     i += 1


# i = 0
# while i <=10:
#     if (i ==5):
#         i+=1
#         break
#     print(i)
#     i +=1


# i = int(input("Enter the number:"))
# while i<=100:
# i = int(input("Enter the number:")) 
# print(i)9


# i = (10,20,30,40,50,60,70,80,90,100,50,50,90,70,50)
# x = 50 
# index = 0
# for val in i:
#     if val == x:
#         print("Number found", index)
#     index = index + 1

# strings = input("enter the strings:")
# strings.split()
# print(strings)


# def avg(a,b,c):
#     return(a+b+c)//3
# res = avg(100,70,50)
# print(res)


#BODY MASS INDEX:
# john = int(67/1.82**2)
# bob = int(80/1.82**2)
# alice = int(50/1.82**2)
# print(john,bob,alice)


# x = 42.201290728
# decimal = x - int(x)
# print(decimal)
# =======
# Write a script that initializes 2 variables n1 and n2 with the values 8 and 9 (accordingly).

# After that initialize another variable n3 that will hold whether n1 is bigger than n2.
# SOLUTION:
# n1=8
# n2=9
# n3=n1!=n2
# print(n3) = True


# b=12
# a=2
# c=(12*2)
# print(c)

# a=20
# b=20
# print(a+b)
  
# length=9
# width=13
# area_of_rectangular=(length*width)
# print(area_of_rectangular)

# num1= int(input("Enter the first number:"))
# num2= int(input("Enter second number"))
# sum=(num1+num2)
# print("Sum of numbers:" , sum)

# num=int(input("Enter the number:"))
# if num %2==0:
#     print("EVEN NUMBER")
# else: print("ODD NUMBER")

# VALUE SWAPPING:
# a=20
# b=90
# print("Before swapping: a=", a, "b=",b)
# a,b=b,a
# print("After swapping:a=",a, "b=",b)
#  Before swapping: a= 20 b= 90
# After swapping:a= 90 b= 20

# TYPE CASTING 
# a=float("5")
# b=10
# print(a+b) = 15.0

# a = int(input("Enter the number1"))
# b = int(input("Enter the number 2"))
# print(a+b)

# l = 4
# w= 4
# print("AREA:",l*w ) 

# a=eval(input("Enter the number 1:"))
# b=eval(input("Enter the number 2:"))
# print(("Average:"), (a+b)/2)

# a=int(input("ENTER THE VALUE:"))
# b=int(input("ENTER THE VALUE:"))
# print(a>=b)

# ENDSWITH FUNCTION:
# str1="I am studying python on Apna College"
# print(str1.endswith("ege"))
# ENDSWITH CHECKS IF STRING ENDS WITH GIVEN STRING
 
# REPLACE FUNTION IS USE TO REPLACE STRING WITH ANOTHER STRING
# str="I am studying python on Apna College"
# print(str.replace("o","a"))
# OUTPUT="I am studying pythan an Apna Callege"

# x = input("Enter your first name:")
# print(len(x))

# str="I have 25$ in my bank account"
# print("RESULT OF YOUR FIND FUNCTION IS:", str.count("$"))


# x = int(input("ENTER THE NUMBER:"))
# if x % 2==0:
#     print("EVEN NUMBER")
# else: print("ODD NUMBER")

# a = int(input("ENTER FIRST NUMBER:"))
# b = int(input("ENTER SECOND NUMBER:"))
# c = int(input("ENTER THIRD NUMBER:"))
# if a>=b and a>=c:
#     print("A IS THE GREATEST")
# elif b>=a and b>=c:
#     print("B IS THE GREATEST")
# elif c>=a and c>=b:
#     print("C IS THE GREATEST")


# x = int(input("Enter the number:"))
# if x %7==0:
#     print(True)
# else: print(False)

# l=[100]
# l.extend([10,20,30,50])
# print(l)

# ADD/APPEND,EXTEND VALUES INTO LIST ALSO SORTING VALUES IN REVERSE IS DOWN BELOW:
# list=[7,10,28,34,67,3,5,9,87,112]
# list.extend([90,100,25,89,1000,988,677])
# list.sort(reverse=True)
# print(list)

# INSERT VALUE IN FUNCTIONS:
# list=[10,20,30,40,50]
# list.insert(2,95)
# print(list)

# value = []
# print(value)
# print(type(value))

# x1 = input("ENTER YOUR FIRT FAV MOVIE NAME:")
# x2 = input("ENTER YOUR SECOND FAV MOVIE NAME:")
# x3 = input("ENTER YOUR THIRD FAV MOVIE NAME:")
# list=[]
# list.extend([x1,x2,x3])
# print(list)


# x=[1,2,3]
# copy_list=x.copy()
# copy_list.reverse()
# if copy_list==x:
#     print("PALINDROME")
# else: print("NOT PALINDROME")

# grade = ("A", "B", "C", "D", "E" "F", "A", "A",)
# print(grade.count("B"))

# list = ["K", "B", "G", "Z", "L", "F",]
# list.sort()
# print(list)

# DICTIONARIES:
# info = {"country" : "pakistan",
#         "age" : "19",
#         "city" : "Islamabad",
#         "village" : "harnal",
#         "name" : "shahzaib ali",}
# print(info ["village"])


# SET DATA TYPE:
# SETS = {1,2,3,3,4,7,7,7, "Hello world", "srring"}
# print(SETS)
# print(type(SETS))
# SET IGNORE DOUBLE VALUES AND IS & UNORDERED. SET IS MUTABLE BUT IT'S ELEMENTS ARE IMMUTABLE (CANNOT BE CHANGED)
#set() is the way to write an empty set


# x=set()
# x.add(1)
# x.remove(1)
# print(x)
 

# dict = {"Car" : "Bugatti Chiron ",
#         "Bike": "Kawasaki Ninja H2R",
#         "Fav SUV" : "Range Rover",
#         "Aimal" : "Cat"
#         }
# print(type(dict))
# print(dict)

# classes  = {"Python", "Java", "C++", "C++", "Javascript", "C++", "Pyhton", "Java"}
# print(len(classes))


# a = int(input("pyshic marks:"))
# b = int(input("math marks:"))
# c = int(input("english marks:"))
# dict = {}
# dict.update({"physics:" : a})
# dict.update({"math:" : b})
# dict.update({"english:" : c})
# print(dict)


# WHILE LOOP:
# i = 2
# while(i<=11):  
#     print(i)
#     i = i + 2 

# a = int(input("Enter the number:"))
# while(True):
#   if a%2 == 0:
#     print(a)

# def GreetHello(): 
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello") 
# print("Executing the function")
# GreetHello() 
# print("Done")
# print("function is finished")

# loop = 100 #Starting point
# while loop >= 1: #Stopping point
#     print(loop) #What yu want to print
#     loop -= 1 #Increment or Decrement
    
# i = 3
# while i <= 30:
#     print(i)
#     i += 3

# i = 1
# while i<=10:
#     print(i*3)
#     i += 1


# i = [10,20,30,40,50,60,70,80,90,100]
# idx = 0
# while idx < len(i):
#     print(i[idx])
#     idx+=1

# nums = (10,20,30,40,50,60,70,80,90,100)
# x= 50
# i=0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found at idx" , i)
#     i +=1


# nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# x = 50
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("Found at idx", i)
#     i += 1


# i = 0
# while i <=10:
#     if (i ==5):
#         i+=1
#         break
#     print(i)
#     i +=1


# i = int(input("Enter the number:"))
# while i<=100:
# i = int(input("Enter the number:")) 
# print(i)9


# i = (10,20,30,40,50,60,70,80,90,100,50,50,90,70,50)
# x = 50 
# index = 0
# for val in i:
#     if val == x:
#         print("Number found", index)
#     index = index + 1

# strings = input("enter the strings:")
# strings.split()
# print(strings)


# Write a script that initializes 2 variables n1 and n2 with the values 8 and 9 (accordingly).

# After that initialize another variable n3 that will hold whether n1 is bigger than n2.
# SOLUTION:
# n1=8
# n2=9
# n3=n1!=n2
# print(n3) = True


# b=12
# a=2
# c=(12*2)
# print(c)

# a=20
# b=20
# print(a+b)
  
# length=9
# width=13
# area_of_rectangular=(length*width)
# print(area_of_rectangular)

# num1= int(input("Enter the first number:"))
# num2= int(input("Enter second number"))
# sum=(num1+num2)
# print("Sum of numbers:" , sum)

# num=int(input("Enter the number:"))
# if num %2==0:
#     print("EVEN NUMBER")
# else: print("ODD NUMBER")

# VALUE SWAPPING:
# a=20
# b=90
# print("Before swapping: a=", a, "b=",b)
# a,b=b,a
# print("After swapping:a=",a, "b=",b)
#  Before swapping: a= 20 b= 90
# After swapping:a= 90 b= 20

# TYPE CASTING 
# a=float("5")
# b=10
# print(a+b) = 15.0

# a = int(input("Enter the number1"))
# b = int(input("Enter the number 2"))
# print(a+b)

# l = 4
# w= 4
# print("AREA:",l*w ) 

# a=eval(input("Enter the number 1:"))
# b=eval(input("Enter the number 2:"))
# print(("Average:"), (a+b)/2)

# a=int(input("ENTER THE VALUE:"))
# b=int(input("ENTER THE VALUE:"))
# print(a>=b)

# ENDSWITH FUNCTION:
# str1="I am studying python on Apna College"
# print(str1.endswith("ege"))
# ENDSWITH CHECKS IF STRING ENDS WITH GIVEN STRING
 
# REPLACE FUNTION IS USE TO REPLACE STRING WITH ANOTHER STRING
# str="I am studying python on Apna College"
# print(str.replace("o","a"))
# OUTPUT="I am studying pythan an Apna Callege"

# x = input("Enter your first name:")
# print(len(x))

# str="I have 25$ in my bank account"
# print("RESULT OF YOUR FIND FUNCTION IS:", str.count("$"))


# x = int(input("ENTER THE NUMBER:"))
# if x % 2==0:
#     print("EVEN NUMBER")
# else: print("ODD NUMBER")

# a = int(input("ENTER FIRST NUMBER:"))
# b = int(input("ENTER SECOND NUMBER:"))
# c = int(input("ENTER THIRD NUMBER:"))
# if a>=b and a>=c:
#     print("A IS THE GREATEST")
# elif b>=a and b>=c:
#     print("B IS THE GREATEST")
# elif c>=a and c>=b:
#     print("C IS THE GREATEST")


# x = int(input("Enter the number:"))
# if x %7==0:
#     print(True)
# else: print(False)

# l=[100]
# l.extend([10,20,30,50])
# print(l)

# ADD/APPEND,EXTEND VALUES INTO LIST ALSO SORTING VALUES IN REVERSE IS DOWN BELOW:
# list=[7,10,28,34,67,3,5,9,87,112]
# list.extend([90,100,25,89,1000,988,677])
# list.sort(reverse=True)
# print(list)

# INSERT VALUE IN FUNCTIONS:
# list=[10,20,30,40,50]
# list.insert(2,95)
# print(list)

# value = []
# print(value)
# print(type(value))

# x1 = input("ENTER YOUR FIRT FAV MOVIE NAME:")
# x2 = input("ENTER YOUR SECOND FAV MOVIE NAME:")
# x3 = input("ENTER YOUR THIRD FAV MOVIE NAME:")
# list=[]
# list.extend([x1,x2,x3])
# print(list)


# x=[1,2,3]
# copy_list=x.copy()
# copy_list.reverse()
# if copy_list==x:
#     print("PALINDROME")
# else: print("NOT PALINDROME")

# grade = ("A", "B", "C", "D", "E" "F", "A", "A",)
# print(grade.count("B"))

# list = ["K", "B", "G", "Z", "L", "F",]
# list.sort()
# print(list)

# DICTIONARIES:
# info = {"country" : "pakistan",
#         "age" : "19",
#         "city" : "Islamabad",
#         "village" : "harnal",
#         "name" : "shahzaib ali",}
# print(info ["village"])


# SET DATA TYPE:
# SETS = {1,2,3,3,4,7,7,7, "Hello world", "srring"}
# print(SETS)
# print(type(SETS))
# SET IGNORE DOUBLE VALUES AND IS & UNORDERED. SET IS MUTABLE BUT IT'S ELEMENTS ARE IMMUTABLE (CANNOT BE CHANGED)
#set() is the way to write an empty set


# x=set()
# x.add(1)
# x.remove(1)
# print(x)
 

# dict = {"Car" : "Bugatti Chiron ",
#         "Bike": "Kawasaki Ninja H2R",
#         "Fav SUV" : "Range Rover",
#         "Aimal" : "Cat"
#         }
# print(type(dict))
# print(dict)

# classes  = {"Python", "Java", "C++", "C++", "Javascript", "C++", "Pyhton", "Java"}
# print(len(classes))


# a = int(input("pyshic marks:"))
# b = int(input("math marks:"))
# c = int(input("english marks:"))
# dict = {}
# dict.update({"physics:" : a})
# dict.update({"math:" : b})
# dict.update({"english:" : c})
# print(dict)


# WHILE LOOP:
# i = 2
# while(i<=11):  
#     print(i)
#     i = i + 2 

# a = int(input("Enter the number:"))
# while(True):
#   if a%2 == 0:
#     print(a)

# def GreetHello(): 
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello") 
# print("Executing the function")
# GreetHello() 
# print("Done")
# print("function is finished")

# loop = 100 #Starting point
# while loop >= 1: #Stopping point
#     print(loop) #What yu want to print
#     loop -= 1 #Increment or Decrement
    
# i = 3
# while i <= 30:
#     print(i)
#     i += 3

# i = 1
# while i<=10:
#     print(i*3)
#     i += 1


# i = [10,20,30,40,50,60,70,80,90,100]
# idx = 0
# while idx < len(i):
#     print(i[idx])
#     idx+=1

# nums = (10,20,30,40,50,60,70,80,90,100)
# x= 50
# i=0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found at idx" , i)
#     i +=1


# nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# x = 50
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("Found at idx", i)
#     i += 1


# i = 0
# while i <=10:
#     if (i ==5):
#         i+=1
#         break
#     print(i)
#     i +=1


# i = int(input("Enter the number:"))
# while i<=100:
# i = int(input("Enter the number:")) 
# print(i)9


# i = (10,20,30,40,50,60,70,80,90,100,50,50,90,70,50)
# x = 50 
# index = 0
# for val in i:
#     if val == x:
#         print("Number found", index)
#     index = index + 1

strings = input("enter the strings:")
strings.split()
print(strings)
