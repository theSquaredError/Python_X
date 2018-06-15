# to get all the winodws 10 spotlight lockscreen wallpaper in the folder

# path =C:\Users\Asus\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets

import os, sys,shutil

path = 'C:\\Users\\Asus\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

current_path = os.getcwd()  #saving the current directory so that we can save our new folder here

current_path = os.path.join(current_path,"lockscreen") #creating a new folder in current directory named "lockscreen"

#if not os.path.exists(current_path):
#	os.makedirs(current_path)

os.chdir(path)

#print(os.getcwd())

for filename in os.listdir(path):

	shutil.copy(os.path.join(path,filename),current_path)

i=1
for filename in os.listdir(current_path):
	shutil.move(filename,"image_" + str(i) +".jpg")
	i=i+1