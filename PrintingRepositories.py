import csv
import os
import FilesCoparing
import HtmlTags
from Variables import headers
from DeleteFiles import delete_folder_01, delete_folder_02, delete_temp_folder


def print_repository(repo):
    print("Repo description: {}".format(repo.description))
    print("Repo active branch is {}".format(repo.active_branch))
    for remote in repo.remotes:
        print("Remote named {} with URL {}".format(remote, remote.url))
    print("Last commit for repo is {}.".format(str(repo.head.commit.hexsha)))

def CSV_write(file_name,dir_path):

    try :
       FilesCoparing.compare_files(file_name,dir_path)
       itensList = HtmlTags.list_of_items
       contentList = HtmlTags.list_of_element
       idsList = HtmlTags.list_of_ids
       typesList = HtmlTags.list_of_types
       mixed_list = [list(item) for item in list(zip(contentList, typesList, idsList, itensList))]
       result = CombineLists(mixed_list)
       temp_file = os.path.join("Report/", file_name + "_Report.csv")

       with open(temp_file, "w", encoding="utf-8", newline="") as fp:
          spamwriter = csv.writer(fp, delimiter=";", quotechar="\n")
          spamwriter.writerow(headers)
          spamwriter.writerows(result)

       clean_Lists(itensList,contentList,idsList,typesList)
    except FileNotFoundError as e:
        print("file/Path not found! Please try again - %s." % ( e.strerror))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except PermissionError as a:
        print("file/Path not found! Please try again - %s." % ( a.strerror))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def CombineLists(mixed_list):
    result = []
    for i in mixed_list:
        if i not in result:
            result.append(i)
    return result

def clean_Lists(*args):
    for elements_List in args:
        elements_List.clear()