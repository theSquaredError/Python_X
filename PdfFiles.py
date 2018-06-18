#!python3
# this script moves all the pdf files in the given path to a new folder

import os, shutil


path = input('Type the path to organise the pdf files:')


if os.path.exists(path):
	os.chdir(path)


#creating a new folder named PdfFiles in the current path

	if not os.path.exists(os.path.join(path,"PdfFiles")):
		os.makedirs(os.path.join(path,"PdfFiles"))



	pathForFolder = os.path.join(path,"PdfFiles")


	for filename in os.listdir():
		if filename.endswith('.pdf'):
			shutil.move(filename,pathForFolder)

	print("Work is completed!!")

else :
	print("Entered path is not valid....")
	