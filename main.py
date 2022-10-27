import HandelingFolders
import PrintingCommits


from Variables import repo, Branch_Name

if __name__ == "__main__":
    repo.git.checkout(Branch_Name)
    PrintingCommits.printing()
    HandelingFolders.Handeling_git_folders()
