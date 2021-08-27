'''
    Title       : Create File String - find common
    Author      : Sarathkumar MC - MT20ACS531
                  Sri Abirami K S - MT20ACS537
    Created on  : Aug 27, 2021
'''
from pathlib import Path
import os

usr_path = "\\MT20ACS537_Sri_Abirami\\2018-08-Hidden-Bee-Elements\\"
file_path = os.getcwd()+usr_path
new_file_path = file_path+"stringpattern\\"
output_file = new_file_path+'common_strings.txt'
file_contents = []

def common(lst):    
    temp_set = set(lst[0])
    for l in lst:
        temp_set = temp_set & set(l) 
    temp_list = list(temp_set)   
    temp_list.sort()    
    return temp_list

if __name__=="__main__":
    try:    
        index = 1        
        for input_file in Path(file_path).iterdir():                
            if not input_file.is_file():
                continue    
            os.system(f'cd {file_path} & mkdir stringpattern & strings "{input_file}" > ./stringpattern/stringpattern_{index}.txt & exit')
            index+=1
            
        for input_file in Path(new_file_path).iterdir():                
            if not input_file.is_file():
                continue            
            with open(input_file, 'r') as temp:
                file_contents.append([i.strip() + '\n' for i in temp.readlines()])
                        
        file = open(output_file,'w')
        for items in common(file_contents):
            file.writelines(items)

        file.close()
    except Exception as e:        
        print(f"{e}\nError occurred, kindly try later!")