import shutil
import os 
import pathlib
desktop = pathlib.Path("USLD")


def output_file(filename):
    return "collected_image/{}".format(filename)
all_code = []
def generate_xml(filename,code):
    xml_code  = """<annotation verified="yes">
        <folder>{}</folder>
        <filename>{}</filename>
        <path>D:\\OneDrive - BUET\\Work\\signlanguage dataset\\USLD\\{}\\{}</path>
        <source>
            <database>Unknown</database>
        </source>
        <size>
            <width>512</width>
            <height>512</height>
            <depth>3</depth>
        </size>
        <segmented>0</segmented>
        <object>
            <name>{}</name>
            <pose>Unspecified</pose>
            <truncated>1</truncated>
            <difficult>0</difficult>
            <bndbox>
                <xmin>1</xmin>
                <ymin>1</ymin>
                <xmax>512</xmax>
                <ymax>512</ymax>
            </bndbox>
        </object>
    </annotation>
    """.format(code,filename,code,filename,code)
    return xml_code


for subdir in desktop.iterdir():
    count = 1
    for file in subdir.iterdir():
        
        count = count + 1
        _,code,filename=file.__str__().split("\\")
        
        new_filename = output_file(f"{code}-{filename}")
        xml_filename = output_file(f"{code}-{filename.split('.')[0]}.xml")
        with open(xml_filename, 'w') as f:
            f.write(generate_xml(new_filename,code))
        shutil.copyfile(file.__str__(),new_filename)
    all_code.append(code)
    print(count)
with open("label.txt", "w") as f:
    for code in all_code:
        f.writelines(code)
        f.writelines("\n")
        
        
                    
