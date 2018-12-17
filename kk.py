import requests
from bs4 import BeautifulSoup
import os,shutil
url = 'http://chrisburkard.com/'

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
print(len(sel_soup.findAll('img')))

images = []

for i in sel_soup.findAll("img"):
    print(i)
    src = i['src']
    images.append(src)

print(images)

current_path = os.getcwd()


iterations = 0
while iterations < 10:    
    for img in images:
        try:
            file_name = os.path.basename(img)    
            img_r = requests.get(img, stream = True)
            new_path = os.path.join(current_path, 'images', 'filename.jpg')
            with open(new_path, 'wb') as output_file:
                shutil.copyfileobj(img_r.raw, output_file)
            del img_r
        except:
            pass
    iterations+=1
    time.sleep(5)
