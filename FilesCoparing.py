import difflib
import filecmp
import os
import sys
import HtmlTags
from Variables import branch_01, branch_02
from DeleteFiles import delete_folder_01, delete_folder_02, delete_temp_folder

def compare_files(file_name, dir_path):
     temp_file = os.path.join("Report/", file_name + "_Report.csv")
     try:
        diff_html = ""
        with open(os.path.join(os.path.join(branch_01,dir_path), file_name), encoding="utf-8") as f1:
            f1_text = f1.readlines()
        with open(os.path.join(os.path.join(branch_02,dir_path), file_name), encoding="utf-8") as f2:
            f2_text = f2.readlines()
        theDiffs = difflib.ndiff(f1_text, f2_text)
        for eachDiff in theDiffs:
          if (eachDiff[0] == "-"):
             diff_html += "<DELETED>|%s|</DELETED>\n" % eachDiff[1:].strip()
          elif (eachDiff[0] == "+"):
            diff_html += "<INSERTED>|%s|</INSERTED>\n" % eachDiff[1:].strip()
        list_of_changes = diff_html.split("\n")
        HtmlTags.print_element(list_of_changes)
     except FileNotFoundError as e:
        os.remove(temp_file)
        print("file/Path not found! Please try again - %s." % ( e.strerror))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     except PermissionError as a:
        os.remove(temp_file)
        print("file/Path not found! Please try again - %s." % ( a.strerror))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        




def compare_folders():
    print("************************************************************************************************************************************")
    comparison = filecmp.dircmp(branch_01, branch_02)
    comparison.report_full_closure()
    print("************************************************************************************************************************************")