# TODO: 1. Write a python program to create a simple function which prints “MySirG” .

# def displaymentorName():
#   i=1
#   while i<=5:
#     print('MySirG')
#     i=i+1
# displaymentorName()

#TODO 2. Write a python program to create a function which expects two arguments and print
# them in the function body.

# def arguments(mentor,course):
#   print(mentor)
#   print(course)
  

# arguments('MySirG','Fullstack WebDev Using Python')

#TODO: 3 Write a python program to create a function which expects an unknown number of arguments.

# def displayNumbers(*n):
#   for i in n:
#     print(i, end= " ")
    
# displayNumbers(10,20,30,40,50)

# TODO: 4 Write a python program to create a function which expects kwargs arguments.

# def displayKeywordArguments(**kwargs):
#   for key, value in kwargs.items():
#     print(key, ":", value)
# displayKeywordArguments(name="deepak",courseTaken= 1, coursename ="Fullstack WebDev Using Python" )

# TODO: 5. Write a python program to create a function which expects a list as an argument.

# def displayList(*n):
#   for i in n:
#     print(i)
# displayList([10,20,30,40])

# def displayList(a):
#   for i in range(len(a)):
#     print(a[i], end=" ")

# list = [10,20,30,40,50]
# displayList(list)

# TODO: 6 . Write a python program to create a function that finds a maximum of four numbers.

# def findMaximum(*n):
#   for i in n:
#     print(max(i))
# findMaximum([10,20,30,40])

#TODO:7. Write a python program to sum all the numbers in a list.

# def findSum(*n):
#   sum = 0
#   for i in n:
#     sum = sum+i
#   print(sum)
# findSum(10,20,30,40)

#TODO: 8 Write a python program to multiply all the numbers in a list.
# def findMultiply(*n):
#   product = 1
#   for i in n:
#     product = product*i
#   print(product)
# findMultiply(10,20)

#TODO: 9. Write a python program to create a function to check whether a number falls in a given range.

# def findNumber(number):
#   numberTofind = 30
#   for i in range(len(number)):
#     if number[i] == numberTofind:
#       print('Yes the number is found at index',i)
#       break
    
# number = [10,20,30,40,50]
# findNumber(number)

# TODO: 10. Write a python program to create a function to check whether a given number is even or odd.

# def evenOdd(number):
#   if number % 2 ==0:
#     print('Its even')
#   else:
#     print('Odd')

# evenOdd(11)


