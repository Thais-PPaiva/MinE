import PrintingRepositories
from BranchCheckout import checkout_branch01, checkout_branch02
from DeleteFiles import delete_folder_01, delete_folder_02, delete_temp_folder
from FilesCoparing import compare_folders, compare_files

def menu():
    while True:
        condition = input("\n Do you want to check any file? (yes/no)  \n ").lower()
        match condition:
            case "no":
             break
            case "yes":
                res = input ("Enter the name of the file to compare: ")
                dire_path = input("Enter the directory of the file you want (if your project do not have any folder just press Enter): ")
                PrintingRepositories.CSV_write(res,dire_path)
            case _:
                print("Invalid Option")

def Handeling_git_folders():
    checkout_branch01()
    checkout_branch02()
    compare_folders()
    menu()
    delete_folder_01()
    delete_folder_02()
    delete_temp_folder()
