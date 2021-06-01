import os

total_numbers = 0
# 当前文件夹中满足条件的文件数
def find_file(filepath, numbers=0):
    file_list = os.listdir(filepath)
    total_numbers = 0
    
    for file in file_list:
        sourcefile = os.path.join(filepath, file)
        if sourcefile.endswith("_gt.json"):
            total_numbers += 1
            
        if os.path.isdir(sourcefile):
            number_sub = find_file(sourcefile, numbers=0)
            total_numbers += number_sub
            
    return total_numbers

filepath = './experiment'
total_numbers = find_file(filepath)
print("Total files =",total_numbers)
