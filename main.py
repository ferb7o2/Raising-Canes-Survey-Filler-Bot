# Selenium Panda Express Bot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains



#change this to the path of the place where you saved chromedriver.exe
locationOfchromeDriver='C:\Program Files (x86)\chromedriver.exe'

def getInfo():
    print("-----------------------------------")
    print("  Raising Canes Filler Bot  ")
    print("-----------------------------------")
    print('please enter your (22 digit) survey code: ')

getInfo(); #2022743744180244071304
    
#prompr user for his code (input)
#code=2022743744180244071304 #for testing purpouses
code='302101329008443222'
    
#Open webdriver (Chrome) and open the panda express survey website
PATH = Service(locationOfchromeDriver)
driver= webdriver.Chrome(service=PATH)
driver.get('https://raisingcane.survey.marketforce.com/?languageId=1')
driver.maximize_window()

codeInputFields = driver.find_elements(By.XPATH,"//input[@type='text']")

act= ActionChains(driver)




counter=0

while len(codeInputFields) != 0:
    codeInputFields[counter].send_keys(code[:4])
    code= code[4:]

    if len(codeInputFields)==0:
        break
    codeInputFields=codeInputFields[1:]

driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"//input[@value='Begin Survey']").click()

driver.find_element(By.XPATH,"//input[@type='text']").send_keys(7.19)
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio']")))
(act.click(on_element=radios[0])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio']")))
(act.click(on_element=radios[1])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio']")))
(act.click(on_element=radios[1])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

print("HELLO WORLD")
radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio']")))
(act.click(on_element=radios[0])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

#how often you visit others
radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio']")))
(act.click(on_element=radios[2])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

cBox = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='checkbox']")))
(act.click(on_element=cBox[1])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='checkbox']")))
(act.click(on_element=radios[0])).perform()
(act.click(on_element=radios[2])).perform()
(act.click(on_element=radios[3])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


for i in range(4):
    radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='5']")))
    (act.click(on_element=radio)).perform()
    driver.find_element(By.XPATH,"//input[@value='Next']").click()

for i in range(3):
    radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio' and @value='5']")))
    (act.click(on_element=radios[0])).perform()
    (act.click(on_element=radios[1])).perform()
    driver.find_element(By.XPATH,"//input[@value='Next']").click()

for i in range(2):
    radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='1']")))
    (act.click(on_element=radio)).perform()
    driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='5']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio' and @value='5']")))
(act.click(on_element=radios[0])).perform()
(act.click(on_element=radios[1])).perform()
(act.click(on_element=radios[2])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='radio' and @value='5']")))
(act.click(on_element=radios[0])).perform()
(act.click(on_element=radios[1])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='1']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='2']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

radios = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@type='checkbox']")))
(act.click(on_element=radios[0])).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='2']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


driver.find_element(By.XPATH,"//input[@value='Next']").click()

for i in range(2):
    radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='1']")))
    (act.click(on_element=radio)).perform()
    driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='3']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='1']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()

for i in range(2):
    radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='2']")))
    (act.click(on_element=radio)).perform()
    driver.find_element(By.XPATH,"//input[@value='Next']").click()

radio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='radio' and @value='1']")))
(act.click(on_element=radio)).perform()
driver.find_element(By.XPATH,"//input[@value='Next']").click()


driver.find_element(By.XPATH,"//input[@placeholder='Name:']").send_keys('Fernando Jaramillo')
driver.find_element(By.XPATH,"//input[@placeholder='Address:']").send_keys('PUT YOUR ADDRESS HERE')
driver.find_element(By.XPATH,"//input[@placeholder='City:']").send_keys('YOUR CITY HERE')
driver.find_element(By.XPATH,"//input[@placeholder='State:']").send_keys('Texas')
driver.find_element(By.XPATH,"//input[@placeholder='Zip:']").send_keys('YOUR ZIP CODE')
driver.find_element(By.XPATH,"//input[@placeholder='Email:']").send_keys('fernando@jaramillo.dev')
driver.find_element(By.XPATH,"//input[@placeholder='Phone:']").send_keys('YOUR PHONE NUMBER HERE')
driver.find_element(By.XPATH,"//input[@value='Next']").click()









time.sleep(400543)


#driver.find_element_by_class_name()

'''

#locate the survey input field & submit button
codeTextfield= driver.find_element(By.ID,'CN1')
nextBtn=driver.find_element(By.ID,'NextButton')


#input the code you entered & click the submit button
codeTextfield.send_keys(str(code))
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000002.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()


time.sleep(3)
higlyBtn=driver.find_element(By.ID,'R000286.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000016.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000013.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000018.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000009.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000012.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(3)
higlyBtn=driver.find_element(By.ID,'R000011.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000287.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000008.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000212.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000010.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000015.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(3)
higlyBtn=driver.find_element(By.ID,'R000021.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000069.2')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000073.5')
driver.execute_script('arguments[0].click()', higlyBtn)
higlyBtn=driver.find_element(By.ID,'R000072.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000078.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000083.2')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000086.2')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
higlyBtn=driver.find_element(By.ID,'R000466.5')
driver.execute_script('arguments[0].click()', higlyBtn)
nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()

time.sleep(1)
drp= Select(driver.find_element(By.ID, 'R000130'))
drp.select_by_visible_text('Male')

drp= Select(driver.find_element(By.ID, 'R000131'))
drp.select_by_visible_text('18 to 24')

drp= Select(driver.find_element(By.ID, 'R000132'))
drp.select_by_visible_text('Under $25,000')

drp= Select(driver.find_element(By.ID, 'R000133'))
drp.select_by_visible_text('Hispanic or Latino')

nextBtn=driver.find_element(By.ID,'NextButton')
nextBtn.click()
time.sleep(400)

my_map = {
    "About me": Hello
}






'''










time.sleep(50);


