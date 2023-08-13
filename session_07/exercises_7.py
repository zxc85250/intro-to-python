# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
# def name():
#   print("My name")

# name()


# # 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
def set_name(name):
  print(name)

# set_name("Yi")

# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
# contact = ["Alice", "Bob", "Charlie"]
# for person in contact:
#   set_name(person)


# 4. Write a function that prints the area of two passed in parameters.
# def area(a,b):
#   print("Area is " + str(a*b))

# area(5,6)


# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
# def print_list(list):
#   for i in list:
#     print(i)
# print_list(["Apple", "Banana", "Orange"])

# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

def age(age):
  if age < 11 and age != 0:
    print("You are too young for this school")
  elif age >= 11 and age <= 16:
    print("You can can come to this school")
  elif age == 0:
    print("You are not born yet!")
  else:
    print("You're too old for school")
  
# age(0)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
def is_odd(num):
  if num % 2 == 1:
    return True
  else:
    return False

# print(is_odd(11))
# print(is_odd(12))

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.

def back(str):
  rev = str[::-1]
  return rev

# print(back("hello"))
# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```
def star(star):
  while star > 0:
    starlist = ""
    for i in range(star):
      starlist += "*"
    print(starlist)
    star -= 1
# star(5)


# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
def padlock(pw):
  if pw == "Unlock":
    print("Unlock")
  else:
    print("Locked")


# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.



# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.



# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
def calc_factorial(x): 
    if x == 1: 
        return 1 
    else: 
        return (x * calc_factorial(x - 1))

num = 4
print(calc_factorial(num))