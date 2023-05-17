# KPMG: Code
## Python — Session 9 — Lesson

---

# Review

---

# For Loops

```python
names = ["Alice", "Bob", "Charlie"]

for person in names:
    print(person)

# Alice
# Bob
# Charlie
```

---

# While Loops

```python
guess = None
while guess != 4:
    # Continues to ask for a number until you enter 4
    guess = int(input("What's your number? "))
```

---

# Collections — List

```python
names = ["Alice", "Bob", "Charlie"]

names.append("Dave") # ["Alice", "Bob", "Charlie", "Dave"]

names[2] = "Chris" # ["Alice", "Bob", "Chris", "Dave"]

del(names[1])# ["Alice", "Chris", "Dave"]

if "Eve" in names:
    print("Eve is here")

for name in names:
    print(name)
```

---

# Collections — Tuple

```python
colours = ("Red", "Blue", "Green")
print(colours[0]) # Red
print(colours[1]) # Blue
print(colours[2]) # Green
```

---

# Collections — Set

```python
fruit = {"Apple", "Banana", "Cherry"}
for item in fruit:
    print(item)
```

---

# Collections — Dictionary

```python
shirt = {
    "size": "Large",
    "colour": "Red"
}

print(shirt["size"]) # Large

shirt["material"] = "Cotton" # Add new key/value pair
shirt["colour"] = "Green" # Change existing value

del(shirt["size"]) # Delete key/value pair

if "material" in shirt:
    print("The material is: " + shirt["material"])

for key in shirt:
    print(str(key) + " = " + str(shirt[key]))
```

---

# Nested Collections

```python
phone_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

for row in phone_grid:
    for column in row:
        print(column)
```

---

# List of Dictionaries

```python
contacts = [
    {"fname": "Alice", "lname": "Smith"},
    {"fname": "Bob", "lname": "Jones", "phone": "555-1234"},
    {"fname": "Charlie", "lname": "McCloud"}
]

for person in contacts:
    if "phone" in person:
        print(person["fname"])
```
---

# Functions

```python
def hello_world():
    print("Hello World!")


hello_world()
```

---

# Functions — Parameters

```python
def hello(name, age):
    print("Hello my name is " + name)
    print("I'm " + str(age) + " years old")

    age_in_10_years = age + 10
    print("In 10 years time I will be " + str(age_in_10_years))


hello("Alice", 22)
hello("Bob", 34)
hello("Charlie", 17)
```

---

# Functions — Returning

```python
def volume(x, y, z):
    return x * y * z


cube1 = volume(12, 3, 4)
cube2 = volume(6, 14, 10)
```

---

# Files — Read

```python
f = open("my_file.txt", "r")
print(f.read())
```

---

# Files — Read

```python
f = open("my_file.txt", "r")
for x in f:
  print(x)
```

---

# Files — Handling

| Value |  Action | Description |
|--- | --- | --- |
| "r" | Read | Opens a file for reading, error if the file does not exist
| "a" | Append | Opens a file for appending, creates the file if it does not exist
| "w" | Write | Opens a file for writing, creates the file if it does not exist
| "x" | Create | Creates the specified file, returns an error if the file exists

---

# Files — Write

```python
f = open("example.txt", "w")
f.write("Hello World")
f.close()

f = open("example.txt", "a")
f.write("It's nice to be here")
f.close()
```

---

# Files — Write

```python
f = open("names.txt", "a")

name = True
while name:
    name = input("Enter a name: ")
    f.write(name + "\n")

f.close()
```

---

## Any Questions?

---


# SDLC, Agile Model, ​Building your first project, Programming Principles, Kanban

---

# SDLC 

---

# What is SDLC?

**SDLC = Software Development Life Cycle.** 

**What is it?** - It is a structured approach followed in the software industry to guide the development of high-quality software applications. 

**What does it consist of?** - The SDLC consists of a series of well-defined phases that encompass the entire software development process, from initial concept and requirements gathering to final deployment and maintenance.

---
# SDLC Stages
---

## Stage 1: Planning And Requirement Analysis

- **Perform requirement analysis** based on inputs from the customers, sales department/market surveys.

- **Conduct product feasibility study** in the economical, operational, and technical areas.

## Stage 2: Defining Requirements

- **All the requirements for the target software are specified** in Software Requirement Specification (SRS) document.

- **Get approval** from the customers, market analysts, and stakeholders.

---

## Stage 3: Designing the Product Architecture

- Based on the SRS, **the design approach for the product architecture is proposed and documented** in a DDS - Design Document Specification.

- **Evaluate the best design** after carrying out risk assessment, product robustness, design modularity, budget, and time constraints.

## Stage 4: Building or Developing the Product

- **The actual development starts** and the product is built.

- Developers must follow the **coding guidelines** defined by their organization.

---

## Stage 5: Testing the Product

- Product defects are reported, tracked, fixed, and retested until the product **reaches the quality standards defined in the SRS**.

## Stage 6: Deployment and Maintenance Of Product

- The conclusive product is **released in phases** as per the organization's strategy and is **tested in a real industrial environment (UAT testing)**.

- After the product is released in the market, its **maintenance** is done for the existing customer base.

---

# Types of SDLC Models

### Following are the most important and popular SDLC models followed in the industry:​

1. **Waterfall Model** – Rigid.​

2. **Iterative Model** – In multiple cycles.​

3. **Incremental Model** – Bit by bit.​


There are also other models like **Spiral Model, V-Model and Big Bang Model**.

---

# How to choose the right SDLC?

### There are some rules that the development crew could use to identify the desired SDLC. These include:​

- The size of the crew​.

- Geographical situation​.

- Size of Software​.

- Complication of software​.

- Types of projects​.

- Business strategies​.

- Engineering capability.

---

# The Agile Model

---

# The Agile Model

- It's a **combination of the iterative and the incremental** process models​.

- Agile Methods break the product into **small incremental builds**. These builds are provided in **iterations**.​

- It's an **adaptive software development method**.

---

# Agile Model - Pros and Cons

---

## Pros:​

- Early customer involvement​.

- Iterative development​.

- Self-organizing teams​.

- Adaptation to change​.


## Cons: ​

- Not suitable for small projects​.

- Depends heavily on customer feedbacks​.

- Not suitable for handling complex dependencies​.

- More risk of maintainability and extensibility.

---

# Building your first project

---

# Task

- Build a **Command-line Program** using Python.​

- It doesn't have to be complicated, **the point of it is for you to create your first project by using the things you learned throughout our lessons**.​

- At the end, you should have a **functioning program, stored on GitHub, with a README.md file containing its description**.

- **DEADLINE:** 1 month from the last session.

---


# Things to consider

- **Respect the project's requirements.**

- The **more challenging your project**, the **less time** you will have to refactor your code.​

- The **less challenging your project**, the **more time** you will have to refactor your code.​

- Think of how you can **personalise the project** so it is unique and an expression of yourself (The language used, ASCII art, etc.).

---

# How to build a successful project?

- **Be consistent.** The more you spend thinking and working on the code, the more solutions and ideas you will have.​

- **Keep track of your kanban board and update it regularly.​**

- When in trouble, **look back to the previous lessons** or **google your problem**. ​

- Try out things and don't be afraid to **experiment**.​

- Many times when you feel stuck, **taking a break** from coding is precisely what you need to refresh.

---

# Programming Principles

---

# Programming Principles

## KISS = Keep it super simple​

- **The simpler the code, the easier to understand, remember and refactor.​**

​
## DRY = Don't repeat yourself​

- **The less repeated elements your code has, the clearer to read and cleaner it will be.**

---

# Kanban

---

# Kanban

## Kanban = Workflow management method.​

- Kanban means **"visual board"** in Japanese.​

- Helps **visualise work, maximize efficiency and  improve continuously.​**

- Started in manufacturing, now **heavily used by Agile software development teams and not only.​**

- Appeared in the late 1940s, as Toyota introduced **"just in time" manufacturing** to its production --> Production based on customer demand, without generating more costs.

---

For info about getting started with your project, head to the **project_info.md** file from the current folder.