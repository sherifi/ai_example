# ==================================
# CREATED BY: SHERIFI
# e-mail: sherif_co@yahoo.com
# git-link for script: https://github.com/sherifi/ai_example.git
# ==================================

# {Windows 10 instructions}
# before you use the script you need to install the dependence
# 1. download the tesseract from the official link:
# 	https://github.com/UB-Mannheim/tesseract/wiki
# 2. install the tesseract
# 	i chosed this path
# 		*replace the user string in the below path with you name of user that you are using in your current machine
# 		C:\Users\user\AppData\Local\Tesseract-OCR\
# 3. Install the  pillow for your python version
# * the best way for me is to install is this form(i'am using python3.7 version and in my CMD i run this version of python by typing py -3.7):
# * if you are using another version of python first look how you start the python from you CMD
# * for some machine the run of python from the CMD is different
	# [examples]
	# =================================
	# PYTHON VERSION 3.7
	# python
	# python3.7
	# python -3.7
	# python 3.7
	# python3
	# python -3
	# python 3
	# py3.7
	# py -3.7
	# py 3.7
	# py3
	# py -3
	# py 3
	# PYTHON VERSION 3.6
	# python
	# python3.6
	# python -3.6
	# python 3.6
	# python3
	# python -3
	# python 3
	# py3.6
	# py -3.6
	# py 3.6
	# py3
	# py -3
	# py 3
	# PYTHON VERSION 2.7
	# python
	# python2.7
	# python -2.7
	# python 2.7
	# python2
	# python -2
	# python 2
	# py2.7
	# py -2.7
	# py 2.7
	# py2
	# py -2
	# py 2
	# ================================
# we are using pip to install the dependences
# because for me i start the python version 3.7 with the following line 
	# py -3.7
# open the CMD in windows machine and type the following line:
	# py -3.7 -m pip install pillow
# 4. Install the  pytesseract and tesseract for your python version
# * the best way for me is to install is this form(i'am using python3.7 version and in my CMD i run this version of python by typing py -3.7):
# we are using pip to install the dependences
# open the CMD in windows machine and type the following lines:
	# py -3.7 -m pip install pytesseract
	# py -3.7 -m pip install tesseract


#!/usr/bin/python
from PIL import Image
import pytesseract
import os
import getpass

def extract_text_from_image(image_file_name_arg):

	# IMPORTANT
	# if you have followed my instructions to install this dependence in above text explanatin
	# for my machine is
	# if you don't put the right path for tesseract.exe the script will not work
	username = getpass.getuser()
	# here above line get the username for your machine automatically
	tesseract_exe_path_installation="C:\\Users\\"+username+"\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
	pytesseract.pytesseract.tesseract_cmd=tesseract_exe_path_installation

	# specify the direction of your image files manually or use line bellow if the images are in the script directory in folder  images
	# image_dir="D:\\GIT\\ai_example\\extract_text_from_image\\images"
	image_dir=os.getcwd()+"\\images"
	dir_seperator="\\"
	image_file_name=image_file_name_arg
	# if your image are in different format change the extension(ex. ".png")
	image_ext=".jpg"
	image_path_dir=image_dir+dir_seperator+image_file_name+image_ext

	print("=============================================================================")
	print("image used is in the following path dir:")
	print("\t"+image_path_dir)
	print("=============================================================================")

	img=Image.open(image_path_dir)
	text=pytesseract.image_to_string(img, lang="eng")
	print(text)

# change the name "image_1" whith the name without extension for your image name
# image_file_name_arg="image_1"
image_file_name_arg="image_2"
# image_file_name_arg="image_3"
# image_file_name_arg="image_4"
# image_file_name_arg="image_5"
extract_text_from_image(image_file_name_arg)

