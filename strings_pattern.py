'''
    Title       : Create File Strings for each files in the file list
    Author      : Sri Abirami K S - MT20ACS537
    Created on  : Aug 27, 2021
'''

import os

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

if __name__=="__main__":
    try:
        file_path = os.path.abspath("./")+"\\MT20ACS537_Sri_Abirami\\2018-08-Hidden-Bee-Elements\\"
        file_list = get_sorted_files(file_path)
        index = 1
        for x in range(len(file_list)):    
            print(os.system(f'cd {file_path} & mkdir stringpattern & strings "{file_list[x]}" > ./stringpattern/stringpattern_{index}.txt & exit'))
            index+=1
    except:
        print("Error occurred, kindly try later!")