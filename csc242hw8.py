import os

def printer(pathname, indent):
    '''prints the pathname of every subfolder contained in folder pathname,
       directly or indirectly, indented in proportion to its depth'''
    print(' ' * indent, pathname)

    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            # n is a subfolder, print it one level deeper
            printer(n, indent + 2)

printer('count',4)
printer('Test',6)

def wordsWithLetterCount(lst,l):
    '''returns the number of words (strings) in the possibly nested list
       lst that contain the letter l, ignoring case'''
    count = 0

    for item in lst:
        if type(item) == list:
            # item is a list, count the words inside it recursively
            count = count + wordsWithLetterCount(item, l)
        elif type(item) == str:
            # item is a word, check if it contains the letter
            if l.lower() in item.lower():
                count = count + 1

    return count

                             
print(wordsWithLetterCount([['','cat',12.0,'dog','MOUSE',1,2,'bird',8,9,10]],'o'))
print(wordsWithLetterCount([],'o'))  
print(wordsWithLetterCount([[[['COMPUTER','science',[[4]],[['animation','art']]]]]],'e'))
        


def uniqueWordsWithLetter(pathname, letter):
    '''returns the set of unique words containing letter found in the files
       contained, directly or indirectly, in folder pathname'''
    words = set()

    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            # n is a folder, add its words using set union
            words = words | uniqueWordsWithLetter(n, letter)
        else:
            # n is a file, check every word in it
            infile = open(n)
            content = infile.read()
            infile.close()

            for word in content.split():
                if letter in word:
                    words.add(word)

    return words

print(uniqueWordsWithLetter('Test','u'))
print(uniqueWordsWithLetter('Test','a'))

def sizer(folder):
    '''returns the total number of characters in all of the files
       contained, directly or indirectly, in folder'''
    total = 0

    for item in os.listdir(folder):
        n = os.path.join(folder, item)

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

print(sizer('Test'))
print(sizer('count'))
print(sizer('Test-2'))

def summary(folder):
    '''returns a string with the contents of all of the files contained,
       directly or indirectly, in folder'''
    result = ''

    for item in os.listdir(folder):
        n = os.path.join(folder, item)

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

print(summary('Test'))
print(summary('count'))
print(summary('Test-2'))  
