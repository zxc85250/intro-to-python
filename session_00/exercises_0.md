# Session 0 Exercises

## Refresher

---

### Bash commands:

```bash
pwd # Prints to the console the path of your current working directory

ls # Lists the files in the directory you are in


cd <directory_name> # Gets in a given directory

cd .. # Gets out of the directory you are in



mkdir <directory_name> # Creates new directory

rmdir <directory_name> # Deletes an empty Directory (Folder)

rm -r <directory_name> # Deletes the directory and its contents recursively


touch <file_name.txt/file_name.py> # Creates new file

rm <file_name.txt/file_name.py> # Deletes file



echo "Hello!"  # Print the text "Hello!" in the terminal window​

echo "Bonjour!" > file.txt  # Writes the text "Bonjour!" in the file.txt file​

cat file.txt  # Reads the file.txt file -> prints the text "Bonjour!" to the console​


history  # Displays your recently run Bash Commands​

clear  # Clears the terminal screen

```

---

### Bash shortcuts:

- TAB - autocompletes commands, file names, or directory names for you​.

- UP/DOWN Arrows - Scroll backward and forwards through previous commands you’ve typed in the current session. ​

---

### Git commands:

```shell

git add . # Adds ALL changes to the staging area in preparation for committing them to the repository.​

git commit -m "<Short description of what you have worked on.>" #  Saves changes to the local repository, along with your commit message, usually describing the changes.

git push origin main # Uploads local changes to your remote repository, on the main branch.
```

---

## Section A

1. Use `pwd` to check in what directory you are.

2. Use `ls` to check what files and folders are in the current directory.

3. Using `cd <directory_name>` go into the `session_00` directory.

4. Create a new folder named `my_first_folder` using `mkdir <directory_name>`.

5. Delete the empty folder `my_first_folder` using `rmdir <directory_name>`.

6. Create a new folder named `animals` using `mkdir <directory_name>`.

7. Get into the `animals` folder by using `cd <directory_name>`.

8. Create 3 text files named `penguin.txt`, `dog.txt`, `bee.txt` by using `touch <file_name.txt>`.
    - Extra challenge: Can you do this while using `touch` only once?

9. Create your first python file called `snake.py` by using `touch <file_name.py>`.

10. Delete the `bee.txt` file with the `rm <file_name.txt>` command.

11.


