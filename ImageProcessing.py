import sys
import os                                     
from PIL import Image

#arguments to hold current dir and  new dir for output  img holder if exists or not

img_folder = sys.argv[1]
output_folder = sys.argv[2]


# to check if outputPokedexImg dir available or notprint(os.path.exists(output_folder))  

if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)  # pass new folder name  on terminal as argument which is stored in output_folder

# looping through the files

for filename in os.listdir(img_folder):
    
    img = Image.open(f'{img_folder}/{filename}')  
    clean_name = os.path.splitext(filename)[0]   
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print("done")
