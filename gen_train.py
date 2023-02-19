

import pathlib
output ='train'
input  ="collected_image"


desktop = pathlib.Path(input)
labels  = []
with open("label.txt", 'r') as f:
    labels=f.read().split("\n")
file_names = []
for file in desktop.iterdir():
    file_names.append(file.__str__())
print(file_names)
    


