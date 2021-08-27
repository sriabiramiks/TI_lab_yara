'''
    Title       : File String - find common
    Author      : Sarathkumar MC - MT20ACS531
                  Sri Abirami K S - MT20ACS537
    Created on  : Aug 27, 2021
'''

import os
from posixpath import sep

def get_sorted_files(Directory):
    try:
        filenamelist = []
        for root, dir, files in os.walk(Directory):
            for name in files:
                fullname = os.path.join(root, name)
                filenamelist.append(fullname)        
        return sorted(filenamelist)
    except:
        print("Error occurred, kindly try later!")

file_path = os.path.abspath("./")+"\\MT20ACS537_Sri_Abirami\\2018-08-Hidden-Bee-Elements\\stringpattern\\"
IMPORT_FILES = get_sorted_files(file_path)
OUTPUT_FILE = file_path+'common_strings.txt'

def common(*lst): 
    return list(set(lst))

file_contents = []
for i in range(len(IMPORT_FILES)):
    temp = 'ip'+str(i+1)
    tempContent = temp+'FileContents'
    with open(IMPORT_FILES[i], 'r') as temp:
        tempContent = temp.readlines()
    tempContent = [i.strip() + '\n' for i in tempContent]
    file_contents.append(tempContent)

file_str_content = str(file_contents)[1:-1]
e = common(file_str_content)
e.sort()

file = open(OUTPUT_FILE,'w')
for items in e:
    file.writelines(items)

file.close()