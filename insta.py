#This is the bot for the instagram
# I use this for getting first 4 images from the page saved to a folder automatically
from selenium import webdriver
import requests,os

driver = webdriver.Chrome()

driver.get('https://instagram.com') 

l = driver.find_elements_by_class_name('izU2O')

login_link = l[0].find_element_by_css_selector('a').get_attribute('href')  #getting the link for the login
driver.get(login_link)

username = ''
password = ''

el3 = driver.find_elements_by_xpath("//*[@class='_2hvTZ pexuQ zyHYP']")
#filling the username
el3[0].send_keys(username)
el3[1].send_keys(password)

#Now clicking the login button

login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button')
login.click()

elements = driver.find_elements_by_class_name("FFVAD")

images = []
i = 0

print(len(elements))
for i in range(len(elements)):
	images.append(elements[i].get_attribute('src'))


os.makedirs('insta',exist_ok=True)
print (len(images))
for i in range(len(images)):
	print (images[i])
	res = requests.get(images[i])
	imageFile = open(os.path.join('insta','img'+str(i+1))+'.jpg','wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

print('Done!')

