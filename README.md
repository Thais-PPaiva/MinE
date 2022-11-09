# TCC-2022.2
Trabalho de conclusão de curso de 2022.2 Sobre mineração repositorios

## Pre-condition
1. Have the python language installed on your computer.
2. Have at least one of the IDE that is necessaries to run the application (Pycharm or VS Code)
3. **Have to have the python on version 3.10 or higher.**
4. **The interpreter used must be a python version equal 3.10 or higher.**

# How to Run the Aplication
1. Use git clone to clone the project.
2. Open the project with the Pycharm IDE or VC code.
3. Open the File Variables.py
4. On the variable REPOSITORY_PATH change the content to path of the repository you want to check (The path is the path of the project on your computer).
5. On the variable Branch_Name Change to the name of the branch you want to check.
6. Open the terminal on the IDE you choose.**
7. Run the command "pip install gitpython"
8. **Go to the file Main.py to run the project.**

PS: If you want to change the amount of the commits showed, change value of the variable COMMITS_TO_PRINT on the file Variables.py.<br>
PS: You need to have the project that you want to check cloned on you computer.<br>
PS: **Do not use "\\" on the repository path always use "/"**<br>

** If you choose to run the aplication the VS Code it will be need to install the python extension for VS Code on your computer.

# How to Generate the CSV file
1. Run the aplication.
2. Choose two commits from the list of commits.
3. Enter the hash of the older commit and wait the process to be finished.
4. Enter the hash of the newest commmit and wait the process to be finished.
5. Enter the name of the file you want to see the diferences (The file name must be provide with the file extension).
6. Enter the path where the desired file is located. (If the especified file is on the main folder, just presss enter).
7. Once the desired HTML file is found the CSV file will be genrated.
8. The generetaed file it will be located on the folder called "Report".

PS: The CSV file will be named with the name of the file that was verified.

## Extras Configurations That Could Be Nesssecessarie
### Change the Python interpreter in the project settings (For Pycharm IDE)
1. Press Ctrl+Alt+S to open the IDE settings and select Project \<project name\> | Python Interpreter.
2. Expand the list of the available interpreters and click the Show All link.
3. Select the target interpreter.<br>
Source: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add_new_project_interpreter<br>

### Interperter configuration (For VS Code)
1. Go to File > Preferences > Settings or Press “Ctrl + ,”.
2. Choose User > Extensions>Python > Python Path and paste the path of where the python is installed.
3. Add “\python.exe” at the end of the path.
4. At the bottom left you will be able to see the python interpreter name.<br>
Source: https://python.plainenglish.io/how-to-set-default-python-interpreter-in-vs-code-76c38c210dc3
##### Find out the python path (For windons)
1. Type python to open the Python shell.
2. Type the following command, and be aware of indentation:<br>
<pre>
import sys
for pth in sys.path:
  print(pth)
</pre>
![image](https://user-images.githubusercontent.com/83622511/200713890-419a6a98-eebc-4c9b-aaed-fa2f4c97084e.png) <br>
Exemple of a python Path <br>
Source: https://python.plainenglish.io/how-to-set-default-python-interpreter-in-vs-code-76c38c210dc3
