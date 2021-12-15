from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver')
driver.get('https://wpcarey.asu.edu/calendarofevents')
height = driver.get_window_size()['height']


for i in range(1,height,int(height/3)):
    last_height = driver.execute_script("window.scrollBy(0, {0});".format(i))
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
    

for i in range(len(RawEventName)):
    print(EventDate[i])
    print(EventName[i])
    print(EventDesc[i])
    

