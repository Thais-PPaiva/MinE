import os
import PrintingRepositories
from Variables import repo, repo_path, COMMITS_TO_PRINT, Branch_Name

# check that the repository loaded correctly
def print_commit(commit):
    print('------------------------------------------------------------------------------------------------------------------------------')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))
    htmlfileInformation = repo.git.diff(commit, '--name-only', '--', '*.html')
    print('Diferences between commit {} and {} "{}"'.format(commit.count(), commit.count() + 1, htmlfileInformation))
    repo.git.checkout(commit.hexsha)


def printing():  # Change the variable
    print("The value of GIT_REPO_PATH is: ", os.environ['GIT_REPO_PATH'])
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        PrintingRepositories.print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits(Branch_Name))[:COMMITS_TO_PRINT]
        print('All commits information:')
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))
