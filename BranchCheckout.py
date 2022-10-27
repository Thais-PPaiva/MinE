from git import GitCommandError
import CopyFiles
from Variables import repo, Branch_Name


def checkout_branch01():
    try:
      print("")
      name = input("Enter the hash of the OLDER commit you want to checkout: ")
      repo.git.checkout(name)
      CopyFiles.coping_folder_01()
      repo.git.checkout(Branch_Name)
    except GitCommandError :
        print("Invalid hash code! Please try again")
        return checkout_branch01()

def checkout_branch02():
    try:
      print("")
      name = input("Enter the hash of the NEWEST commit you want to checkout: ")
      repo.git.checkout(name)
      CopyFiles.coping_folder_02()
      repo.git.checkout(Branch_Name)
    except GitCommandError :
        print("Invalid hash code! Please try again")
        return checkout_branch02()
