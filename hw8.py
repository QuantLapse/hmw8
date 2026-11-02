# CSC 241 - Assignment 8
# Recursion
#
# All of the folder problems below follow the same pattern as the
# antivirusredux.py example from class:
#   - loop through the contents of the folder with os.listdir()
#   - build the full pathname of each item with os.path.join()
#   - if the item is a folder, make a recursive call on it
#   - otherwise the item is a file, so open it and read it

import os


# Problem 1
def printer(pathname, indent):
    '''prints the pathname of folder pathname and of every subfolder
       contained in it, directly or indirectly, indented in proportion
       to its depth with respect to the topmost folder'''
    print(' ' * indent, pathname)

    for item in os.listdir(pathname):
        # create the pathname for item
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            # n is a subfolder, so print it (and its subfolders)
            # one level deeper
            printer(n, indent + 2)


# Problem 2
def wordsWithLetterCount(lst, letter):
    '''returns the number of words (strings) in the possibly nested
       list lst that contain letter, ignoring case'''
    count = 0

    for item in lst:
        if type(item) == list:
            # item is a list, so count the words inside it recursively
            count = count + wordsWithLetterCount(item, letter)
        elif type(item) == str:
            # item is a word, check if it contains the letter
            if letter.lower() in item.lower():
                count = count + 1
        # anything else (int, float, ...) is not a word, so skip it

    return count


# Problem 3
def uniqueWordsWithLetter(pathname, letter):
    '''returns the set of unique words that contain letter, found in the
       files contained, directly or indirectly, in folder pathname'''
    words = set()

    for item in os.listdir(pathname):
        # create the pathname for item
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            # n is a folder, add its words using set union
            words = words | uniqueWordsWithLetter(n, letter)
        else:
            # n is a file, read it and check every word in it
            infile = open(n)
            content = infile.read()
            infile.close()

            for word in content.split():
                if letter in word:
                    words.add(word)

    return words


# Problem 4
def sizer(pathname):
    '''returns the total number of characters in all of the files
       contained, directly or indirectly, in folder pathname'''
    total = 0

    for item in os.listdir(pathname):
        # create the pathname for item
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            # n is a folder, add the size of its files recursively
            total = total + sizer(n)
        else:
            # n is a file, add the number of characters in it
            infile = open(n)
            content = infile.read()
            infile.close()

            total = total + len(content)

    return total


# Problem 5
def summary(pathname):
    '''returns a string containing the contents of all of the files
       contained, directly or indirectly, in folder pathname'''
    result = ''

    for item in os.listdir(pathname):
        # create the pathname for item
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            # n is a folder, add the contents of its files recursively
            result = result + summary(n)
        else:
            # n is a file, add its contents
            infile = open(n)
            content = infile.read()
            infile.close()

            result = result + content

    return result
