import shutil
from Variables import REPOSITORY_PATH, branch_01 , branch_02
from DeleteFiles import delete_git_folder_01, delete_git_folder_02

def coping_folder_01():
    shutil.copytree(REPOSITORY_PATH, branch_01)
    delete_git_folder_01()

def coping_folder_02():
    shutil.copytree(REPOSITORY_PATH, branch_02)
    delete_git_folder_02()
