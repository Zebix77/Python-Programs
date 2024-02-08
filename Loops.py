# for loop
# Increment
# for x in range(3,30,3):
#     print(x)
# Decrement
# for x in range(10,1,-2):
#     print(x)
# for n in range(10):
#     print("Zebi")
# while loop:
# x=1
# while x<=10:
#     print("Zebix77")
#     x=x+1 
# for x in range(9,90,9):
#     print(x)
# x=1
# while x<=15:
#     print("Zebi")
#     x=x+5


# x = 1 
# n = eval(input("Enter the number:"))
# while x <=10:
#     print(n*x)
#     x+=1 

# x = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(x):
#     print(x[idx])
#     idx += 1

# num = (10,20,30,40,50,60,70,80,90,100)
# x = 90
# idx = 0
# while idx < len(num):
#     if (num[idx]) == x:
#         print("Found at", idx)
#     idx += 1

# i = 0
# while i<=5:
#     if (i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1
 

# cars = ["Audi", "BMW", "Mercedes", "VW", "Porsche", "Lamborghini"]
# for x in cars:
#     print(x, end= " ")


# num = (1,2,3,4,5,6,7,8,9,10,7,90,7)
# x = 7
# idx = 0
# for n in num:
#     if n == x:
#         print("Found at idx:", idx)
#     idx +=1



#FIND FACTORIAL USING WHILE LOOP
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Answer is:" , fact)

n = int(input("Enter the number:"))
fact = 1
for i in range(1,n+1):
    fact *= i 
    print("Factorial:", fact)