import os
import git
from git import Repo

COMMITS_TO_PRINT = 10
REPOSITORY_PATH = ""
TEMP_FOLDER = "Temp/"

Branch_Name = "main"
repo_path = git.Repo(REPOSITORY_PATH)
os.environ["GIT_REPO_PATH"] = REPOSITORY_PATH
repo_path = os.getenv("GIT_REPO_PATH")
repo = Repo(repo_path)

branch_01 = os.path.join(TEMP_FOLDER,"Branch_01/")
branch_02 = os.path.join(TEMP_FOLDER,"Branch_02/")


#Lists used
headers = ["Element", "type", "id", "code"]
list_of_tags = ["<tittle", "<p", "<label", "<select", "<option", "<input", "<h", "<div", "<footer",
                "<header", "<nav", "<section", "<li", "<ol", "<ul", "<img", "<video", "<picture", "<del",
                "<button", "<form", "<legend", "<output", "<textarea", "<details", "<content"]
list_of_items = []
list_of_element =[]
list_of_ids = []
list_of_types = []
