# TCC-2022.2
Trabalho de conclusão de curso de 2022.2 Sobre mineração repositorios

## Pre-condition
1. Have the python language installed on your computer
2. Have at least one of the IDE that is nescessarie to run the application (Pycharm or VS Code)
3. **Have to has the python on version 3.10 or higther.**
4. **The interpreter used must be a python version equal 3.10 or highter.**

# How to Run the Aplication
1. Use git clone to clone the project.
2. Open the project with the Pycharm IDE or VC code.
3. Open the File Variables.py
4. On the variable REPOSITORY_PATH change the content to path of the repository you want to check (The path is the path of the project on your computer).
5. On the variable Branch_Name Change to the name of the branch you want to check.
6. Open the terminal on the IDE you choose.**
7. Run the command "pip install gitpython"
8. **Go to the file Main.py to run the project.**

PS: If you want to change the amount of the commits showed, change value of the variable COMMITS_TO_PRINT on the file Variables.py.
PS: You need to have the project that you want to check cloned on you computer.
PS: **Do not use "\\" on the repository path always use "/"**

** If you choose to run the aplication the VS Code it will be need to install the python extension for VS Code on your computer.

# How to Generate the CSV file
1. Run the aplication.
2. Choose two commits from the list of commits.
3. Enter the hash of the older commit and wait the process to be finished.
4. Enter the hash of the newest commmit and wait the process to be finished.
5. Enter the name of the file you want to see the diferences.
6. Enter the path where the desired file is located. (If the especified file is on the main folder, just presss enter).
7. Once the desired HTML file is found the CSV file will be genrated.
8. The generetaed file it will be located on the folder called "Report".

PS: The CSV file will be named with the name of the file that was verified.
