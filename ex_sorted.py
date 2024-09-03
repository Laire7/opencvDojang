# numbers = ["20240903_11", "20240903_12", "20240903_13"]
import os
folderName = os.listdir('test')
#print(folderName)
sorted_numbers_desc = sorted(folderName, reverse=False)
print(f'정렬: {sorted_numbers_desc}')

sorted_folder_list = sorted(folderName, key=lambda x: tuple(map(int, x.split('_'))))
print(sorted_folder_list)