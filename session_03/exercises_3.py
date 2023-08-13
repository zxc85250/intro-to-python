# # Session 3 Exercises

# ## Section A
# # 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
# # name = input("what's your name? ")
# # if name == "Bob":
# #   print("Welcome Bob")

# # # 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
# # name = input("what's your name? ")
# # if name != "Alice":
# #   print("You're not Alice!")


# # 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
# #   If they get it wrong, print "Password failure".
# # password = input("What's your password? ")
# # if password == "qwerty123":
# #   print("You have successfully logged in")
# # else:
# #   print("Password failure")
  


# # 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
# # num = int(input("Enter a number: "))
# # if num%2 == 0:
# #   print("Even")
# # else:
# #   print("Odd")

# # 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
# # num1 = int(input("Enter num1: "))
# # num2 = int(input("Enter num2: "))

# # if num1 + num2 > 21:
# #   print("Bust")
# # else:
# #   print("Safe")

# # 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
# # length = input("Enter length: ")
# # width = input("Enter width: ")
# # if length == width:
# #   print("Square")
# # else:
# #   print("NA")

# # 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
# #   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# # year = int(input("Enter service year: "))
# # salary = int(input("Enter your salary: "))

# # if year > 3:
# #   print("Your bouns: " + str(salary * 0.1))
# # else:
# #   print("No bonus")


# # 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
# # num = int(input("Enter a number: "))
# # if num > 0:
# #   print(num*3)
# # else:
# #   print(num/2)



# # <---------------------------------------------------------------------------------------------->

# ## Section B
# # 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
# #   print "You're not Bob! I'm Bob", else print "You must be Charlie".
# name = input("Enter a name: ")
# if name == "Alice":
#   print("Hello, Alice")
# elif name == "Bob":
#   print("You're not Bob! I'm Bob")
# else:
#   print("You must be Charlie")


# # 2. Ask the user to enter their age:
# #     1. If they are younger than 11, print "You're too young to go to this school"
# #     2. If they are between 11 and 16, print "You can can come to this school"
# #     3. If they are over 16, print 'You're too old for school"
# #     4. If they are 0, print "You're not born yet!"
# age = int(input("Enter your age: "))

# if age < 11:
#   print("You're too young to go to this school")
# elif age >= 11 and age <= 16:
#   print("You can can come to this school")
# elif age > 16:
#   print("You're too old for school")
# elif age == 0:
#   print("You're not born yet!")
  
# # 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
# #     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
# #     2. Ensure that when an unknown month is given it prints "I don't know".

# month = input("Enter month: ")

# if month == "March" or month == "April" or month == "May":
#   print("Spring")
# else:
#   print("I don't know")

# # 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
# numb1 = int(input("Enter num1: "))
# numb2 = int(input("Enter num2: "))

# if numb1%2 == 0 and numb2%2 == 0:
#   print("Even")
# elif numb1%2 == 1 and numb2%2 == 1:
#   print("Odd")
# else:
#   print("I don't know")

# # 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# if num1 > num2:
#   print(num1)
# else:
#   print(num2)


# # 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
# #   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
# #    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# year = int(input("Enter service year: "))
# salary = int(input("Enter salary: "))

# if year > 7:
#   print(salary * 0.2)
# elif year > 5:
#   print(salary * 0.15)
# elif year >= 3 and year <= 5:
#   print(salary * 0.1)
# else:
#   print("No bonus")


# # 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
# #   If all three ages are the same, print that.
# age1 = int(input("Enter age1: "))
# name1 = input("Enter name1: ")
# age2 = int(input("Enter age2: "))
# name2 = input("Enter name2: ")
# age3 = int(input("Enter age3: "))
# name3 = input("Enter name3: ")

# if age1 > age2 and age1 > age3:
#   print(name1)
# elif age2 > age1 and age2 > age3:
#   print(name2)
# elif age3 > age1 and age3 > age2:
#   print(name3)
# else:
#   print("same")
# # 8. A school has following rules for their grading system:
# #     a.	Above 80 – A
# #     b.	60 to 80 – B
# #     c.	50 to 60 – C
# #     d.	45 to 50 – D
# #     e.	25 to 45 – E
# #     f.	Below 25 - F
# #   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

