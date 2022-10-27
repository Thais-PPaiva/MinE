import os
import stat
import shutil
from Variables import branch_01, branch_02, TEMP_FOLDER


def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def delete_git_folder_01():
    for i in os.listdir(branch_01):
       if i.endswith('.git'):
           tmp = os.path.join(branch_01, i)
           while True:
               break
           shutil.rmtree(tmp, onerror=on_rm_error)

def delete_git_folder_02():
    for i in os.listdir(branch_02):
       if i.endswith('.git'):
           tmp = os.path.join(branch_02, i)
           while True:
               break
           shutil.rmtree(tmp, onerror=on_rm_error)

def delete_folder_01():
    try:
        delete_git_folder_01()
        shutil.rmtree(branch_01, ignore_errors=True)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

def delete_folder_02():
    try:
        delete_git_folder_02()
        shutil.rmtree(branch_02, ignore_errors=True)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

def delete_temp_folder():
    try:
        shutil.rmtree(TEMP_FOLDER, ignore_errors=True)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
