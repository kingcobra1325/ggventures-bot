from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

link = "https://wpcarey.asu.edu/calendarofevents"


options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--headless')
options.add_argument('--log-level 3') 
driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
driver.get(link)
height = driver.execute_script("return document.body.scrollHeight")


for i in range(1,height,int(height/5)):
    driver.execute_script("window.scrollBy(0, {0});".format(i))
    sleep(0.5)


RawEventName = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'col-sm-10')]/h3")))
RawEventDesc = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'col-sm-10')]/p[contains(@class, 'info')]")))
RawEventDateM = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'date-badge full-date')]/span[contains(@class, 'month')]")))
RawEventDateD = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'date-badge full-date')]//span[contains(@class, 'date-display-single')]")))


EventName = list()
EventDesc = list()
EventDate = list()

for i in range(len(RawEventName)):
    EventName.append(RawEventName[i].text)
    EventDesc.append(RawEventDesc[i].text)
    EventDate.append(RawEventDateM[i].text+' '+ RawEventDateD[i].text)
    
    print(EventName)
    print(EventDesc)
    print(EventDate)