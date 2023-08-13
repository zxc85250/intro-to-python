import random
import string

def password_gen(length, num_only):
  password = ""
  if num_only == "n":
    for i in range(int(length)):
      rand_int_letter_symbol = random.randint(0, 2)
      if rand_int_letter_symbol == 0:
        password += random.choice(string.ascii_letters)
      elif rand_int_letter_symbol ==1:
        password += random.choice("$%@?£&")
      else:
        password += str(random.randint(0,9))
  else:
    for i in range(int(length)):
      password += str(random.randint(0,9))
  return password

Num_contact = int(input("How many people would you want to create password for?\n"))
Contact = []
while Num_contact!=0:
  name = input("Please enter the account / platform / user name:\n")
  decision_length = int(input("Please enter the length of user's password:\n"))
  decision_combine = input("Does user's password contain numbers only [y/n]?\n")

  while decision_combine != "y" and decision_combine != "n":
    decision_combine = input("Please confirm whether your password contains number only or not [y/n]?\n")

  password = password_gen(decision_length, decision_combine)
  Contact.append(
    {"Name" : name, "Password" : password}
  )
  Num_contact -= 1
  
print(Contact)