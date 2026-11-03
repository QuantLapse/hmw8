
import os
def fileStartsWithCount(folder,chars):
    '''returns the number of files, in folder and all of its
       subfolders, whose name starts with chars'''
    count = 0
    for item in os.listdir(folder):     # for every file or folder in folder
        n = os.path.join(folder, item)  # create pathname for item (any OS)
        try:
            # blindly recurse on n, add the count found in that subfolder
            count += fileStartsWithCount(n, chars)
        except:
            # base case: exception means that n is a file
            if item.startswith(chars):
                count += 1
    return count


def countDir(path, dname):
    '''returns the number of directories named dname (any
       capitalization) found in the path directory structure'''
    count = 0
    for item in os.listdir(path):       # for every file or folder in path
        n = os.path.join(path, item)    # create pathname for item (any OS)
        try:
            # blindly recurse on n, add the count found in that subfolder
            count += countDir(n, dname)
            # no exception, so n is a directory: check its name
            if item.lower() == dname.lower():
                count += 1
        except:
            # exception means that n is a file, so nothing to count
            pass
    return count
