# [fit] KPMG: Code
## [fit] Python — Session 6 — Lesson

---

# [fit] OS, CLI, GIT & IDE​s

---

# Objectives

- Brief overview of Operating Systems​
- Understand Terminal/CLI​
- Understand Source Control Management & Git​
- Brief overview of Markdown and IDEs

---

# [fit] Operating Systems (OS)

---

# Operating systems (OS)

 - Software that communicates with machine hardware.​

 - Can you name some popular examples? 

 ---

# Operating systems

- Some include a graphical user interface (GUI) for manipulation (Windows, MAC OS)​

- Linux has multiple distributions - some can include a GUI (e.g. Ubuntu) while some don’t.​

- When would we want or not want to have a GUI?

---

# Linux

- Popular operating system based on UNIX​

- Open-source, multiple distributions​

- Commonly used for hosting web servers and scientific computing

---

# [fit] Command-line Interface (CLI) and Bash

---


# CLI - Command Line Interface

- Also referred to as the ‘Console’ or ‘Terminal’.​

- Terminal app on your Mac (you will have it by default because Mac OS is UNIX based) or Git Bash on your Windows (needs downloading)

---

# Bash - Bourne Again SHell

- Command Language for most Linux distributions​

- sh = Bourne Shell​

- The Shell is the layer between the Operating System and the User (or other services)

---

# Bash commands

```bash
pwd # Prints to the console the path of your current working directory

ls # Lists the files in the directory you are in


cd <directory_name> # Gets in a given directory

cd .. # Gets out of the directory you are in

```

---

# More bash commands

```bash
mkdir <directory_name> # Creates new directory

rmdir <directory_name> # Deletes an empty Directory (Folder)

rm -r <directory_name> # Deletes the directory and its contents recursively


touch <file_name.txt/file_name.py> # Creates new file

rm <file_name.txt/file_name.py> # Deletes file


mv original_file1 /home/newfile1 # Moves a file (can be used for renaming) ​

cp original_filename copy_filename # Makes a copy of a file

```

---

# More bash commands

```bash
echo <text> # Displays in the terminal a line of text, Ex: echo Hello!

echo <text> > <file_name.txt>  # Writes a line of text in a file, Ex: echo Bonjour! > file.txt

cat <file_name.txt> # Reads the file and displays it line by line in the terminal, Ex: cat file.txt --> Bonjour!


history  # Displays your recently run Bash Commands​

date # Displays the date

man <command> # Displays the manual and description for the chosen command -> ex: man ls/pwd/cd/mkdir


clear  # Clears the terminal screen



```

---

# Bash shortcuts

- TAB - autocompletes commands, file names, or directory names for you​.

- UP/DOWN Arrows - Scroll backward and forwards through previous commands you’ve typed in the current session. ​

- F3 - Repeat the previous command​.

- CTRL + C -  Abort the current line you’re typing or a command that is currently executing​.


---

# [fit] Source Control Management(SCM) and Git

---


# Source Control Management(SCM)

- Refers to tools used to track modifications to a source code repository.​

- Source Control Management = Version Control​

---

# Why do we use Source Control?

- Helps teams work collaboratively.

- Developers can edit shared code without unknowingly overwriting each other’s work.

- Serves as a protection mechanism.


--- 

# Git

- Git (Global Information Tracker) = a version control system.​

- Why Git? ​-> Because of its popularity, community, opensource nature, and decentralised approach.

---

# Git - What does it do?

- Allows you to *collaborate* on a project without interfering with each other’s work.​

- Keeps a historical record of everyone's work so you can go back to previous records.​

- You can work on your local copy of the codebase and then merge your changes with the main codebase.​

- Uses a series of snapshots, called commits, to track changes to the codebase over time along with the timestamp and user who made the changes.

---

# Terminology

### Remote Repository​

- This is where everyone shares their code centrally (ex: GitHub). ​


### Local Repository​

 - When you commit your code, a local version is created on your machine.

 ---

 # Basic Git commmands

 ```bash
git clone <https://github.com/sergiuHudrea/intro-to-python.git>  # Copies an existing Git repository from a remote location to your local machine.​


git init  # Initializes an existing directory as a Git repository.


git status  # Shows the current status of the repository, including which files have been modified, which files have been added to the staging area, and which files are not being tracked by Git.
 ```

 ---

 # Basic Git commands

 ```bash

git add . # Adds ALL changes to the staging area in preparation for committing them to the repository.​

git commit -m "<Short description of what you have worked on.>" #  Saves changes to the local repository, along with your commit message, usually describing the changes.

git push origin main # Uploads local changes to your remote repository, on the main branch.

git pull  origin main # Downloads changes from the remote repository (main branch) and incorporates them into your local repository.

 ```

---

# Markdown and IDEs

---

# Markdown and README.md

- When creating a repository, you usually start off by writing a **README.md** file in a Markup language called Markdown.​

- The **README.md** summarises important information about the contents of the repo, instructions on how to edit or run the software, etc.​

- *Markdown* is a lightweight markup language for creating formatted text using a plain-text editor.


---

# IDEs

- **IDE** = An Integrated development environment is a software for application building. It combines tools into a single graphical user interface (GUI).​

- Why use an IDE? ​--> The tools needed are already there and ready to use. It is efficient and makes life easier.​

- Imagine repairing a car in a parking lot VS repairing it in a garage.​

- You can develop applications without an IDE, but the you would have to build your own IDE by manually integrating the tools you need.​

- Replit = a cloud IDE --> No need for downloading software and configuring local environments. No more "But it works on my machine".

---