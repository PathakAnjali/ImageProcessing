# IMAGE PROCESSING PROJECT
import sys
import os  # to grab the path
from PIL import Image

# step1: arguments to hold current dir and  new dir for output  img holder if exists or not

img_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(img_folder,output_folder)


# to check if outputPokedexImg dir available or not
print(os.path.exists(output_folder))  # gives Boolean value if folder exists or not

if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)  # pass new folder name  on terminal as argument which is stored in output_folder

# loop through the files present in the PokedexConvertorImg dir

for filename in os.listdir(img_folder):  # as img_folder is the input folder,to loop through
    img = Image.open(f'{img_folder}/{filename}')  # '/' is added as to navigate the folder and file name
    clean_name = os.path.splitext(filename)[0]    # to avoid this type filename > charmander.jpg.png > to remove .jpg
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print("done")
