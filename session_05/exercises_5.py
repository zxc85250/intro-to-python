# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
import random

# for i in range(10):
#   print(random.randint(1, 10))

# # 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
# #     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
# number = random.randint(1, 10)
# guess = None
# while guess != number:
#   guess = int(input("Enter a number: "))

# print("Lucky!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

import math

# height = int(input("Please enter the height: "))
# width = int(input("Please enter the width: "))
# area = math.ceil(height * width / 10000)
# print(area)
# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
# password = "qwerty123"
# userpassword = input("What is your password?\n")
# times = 0

# while times < 2:
#   if userpassword == password:
#     print("You have successfully logged in")
#     break
#   else:
#     print("Password failure")
#     userpassword = input("What is your password?\n")
#     times+=1
    
# if times == 2:
#   print("System Locked!")

# 5. Add up all the numbers from 1 to 500 and print the answer.
# allnum = 0
# for i in range(1, 501):
#   allnum +=i
# print(allnum)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
# num = []
# for i in range(10):
#   ans = int(input("Please enter number:\n "))
#   num.append(ans)
# ins = num.index(99)
# print(ins)

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
# num1 = 1
# while num1 < 16:
#   print(str(num1) + " x 18")
#   num1+=1


# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
# i = 0
# while i < 101:
#   print(i)
#   i+=1


# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
# import random
# prize_draw_list = []
# user_input = None

# # while the user does not enter a blank space, keep asking for names to be added to the draw
# while user_input != "":
#     user_input = input("Please input your name to be added to the prize draw:\n")
#     # only if the user enters a name and not an empty string will it be added to the prize draw list
#     if user_input != "":
#         prize_draw_list.append(user_input)
# print("Congratulations! " + random.choice(prize_draw_list) + " you are the winner of the prize draw!")

# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

sum = 0 
i = 0
while i < 10: 
    i += 1 
    sum += i
print(sum)
