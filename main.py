# Selenium Panda Express Bot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#change this to the path of the place where you saved chromedriver.exe
locationOfchromeDriver='C:\Program Files (x86)\chromedriver.exe'

def getInfo():
    print("-----------------------------------")
    print("  Panda Express Survey Filler Bot  ")
    print("-----------------------------------")
    print('please enter your (22 digit) survey code: ')

getInfo();
    #code=1234567890123456789012 #for testing purpouses
#prompr user for his code (input)
code=input()
    
#Open webdriver (Chrome) and open the panda express survey website
PATH = Service(locationOfchromeDriver)
driver= webdriver.Chrome(service=PATH)
driver.get('https://www.pandaguestexperience.com/?AspxAutoDetectCookieSupport=1')

#locate the survey input field & submit button
codeTextfield= driver.find_element(By.ID,'CN1')
nextBtn=driver.find_element(By.ID,'NextButton')

#input the code you entered & click the submit button
codeTextfield.send_keys(str(code))
nextBtn.click()


time.sleep(5);


