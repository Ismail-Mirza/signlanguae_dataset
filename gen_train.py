

import pathlib
import shutil
output ='train'
input  ="collected_image"


desktop = pathlib.Path(input)
labels  = []
with open("label.txt", 'r') as f:
    labels=f.read().split("\n")
file_names = []
for file in desktop.iterdir():
    file_names.append(file.__str__())
count = 0
for file_name in file_names:
    print(file_name)
    count += 1
    if count <=80:
        shutil.copy(file_name,"train\\"+file_name.split("\\")[1])
    if count>80 and count <=100:
        shutil.copy(file_name, "test\\"+file_name.split("\\")[1])
    if count == 100:
        count = 0
    
        
        
        
    


