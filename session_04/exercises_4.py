# # Session 4 Exercises

# ## Section A
# # 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
# fruit = ["Apple", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
# # print(fruit)


# # 2. Add "Grapes" to the list and print the list.
# fruit.append("Grapes")
# print(fruit)


# # 3. Change "Pears" to "Strawberries" and print the list.
# fruit[2] = "Strawberries"
# print(fruit)

# # 4. Remove "Apples" from the list and print the list.
# del(fruit[0])
# print(fruit)


# # 5. Print out the current length of the list.
# print(len(fruit))


# # 6. Order the list alphabetically.
# fruit.sort()



# # 7. Print out the list again.
# print(fruit)



# # <---------------------------------------------------------------------------------------------->

# ## Section B
# # 1. Loop through the list you created in section A and print each item out.
# for i in fruit:
#   print(i)


# # 2. Print the numbers 1 to 100 (including the number 100).
# for num in range(1,101):
#   print(num)


# 3. Print all odd numbers from 1 to 100.
# for num in range(1,101,2):
#   print(num)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
# olylist = [1916, 1940, 1944, 2020]
# for oly in range(1896, 2023, 4):
#   if oly not in olylist:
#     print(oly)


# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
# num = [13,24,56,72,50,67,234,11,79,34]
# num1 = 0
# num2 = 0
# for i in num:
#   if i%2 == 0:
#     num1+=1
#   else:
#     num2+=1
# print(num1, num2)

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
# names = ["Amy", "Bob", "Clay", "Dan", "Eva"]
# for i in names:
#   print("Hello " + i)


# # 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

# for i in "supercalifragilisticexpialidocious":
#   print(i)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
# l1 = [1,2,3,4,5]
# l2 = []

# for i in l1:
#   l2.append(i**2)
  
# print(l2)
# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
# name1 = ["Amy", "Bob", "Clay", "Dan", "Eva"]
# name2 = []
# for i in name1:
#   name2.append("Dr."+ i)
# print(name2)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
for x in range(1, 10, 2):
    print(x)