# from time import sleep

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException


# def tryXPATH(driver,isList,isFirst,tempPath,hasAttrib = None):
#     try:
#         if isList and isFirst:
#             return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,tempPath)))
#         elif isList:
#             return driver.find_elements(By.XPATH,tempPath)
#         elif not isList and hasAttrib and isFirst:
#             return (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,tempPath)))).get_attribute(hasAttrib)
#         elif not isList and isFirst:
#             return (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,tempPath)))).text
#         else:
#             return driver.find_element(By.XPATH,tempPath).text
#     except Exception as e:
#         print(e)
#         #logger.error()
#         return ''
    

# link = "https://zicklin.baruch.cuny.edu/"

# event_name = list()
# event_date = list()
# event_time = list()
# event_desc = list()

# options = webdriver.ChromeOptions()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# options.add_argument(f'user-agent={user_agent}')
# # options.add_argument('--headless')
# options.add_argument('--log-level 3') 
# driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
# getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
# driver.get(link)
# height = driver.execute_script("return document.body.scrollHeight")


# for i in range(1,height,int(height/5)):
#     driver.execute_script("window.scrollBy(0, {0});".format(i))
#     sleep(0.5)
    
# logo = tryXPATH(driver,False,True,"//div[contains(@class,'zk-print-logo')]/img[contains(@id,'dtlogo')]",'src')

# driver.get("https://zicklin.baruch.cuny.edu/events/")

# while True:
#     EventLinks = tryXPATH(driver,True,True,"//a[contains(@class,'tribe-event-url news-listing-title')]")

#     for i in EventLinks:
#         getter.get(i.get_attribute('href'))
        
#         RawEventName = tryXPATH(getter,False,True,"//h1[contains(@class,'tribe-events-single-event-title')]")
        
#         RawEventDesc = tryXPATH(getter,False,False,"//div[starts-with(@class, 'tribe-events-single-event-description tribe-events-content')]/p[1]")
        
#         RawEventDate = tryXPATH(getter,False,False,"//abbr[contains(@class,'tribe-events-abbr tribe-events-start-date published dtstart')]")
        
#         RawEventTime = tryXPATH(getter,False,False,"//div[contains(@class,'tribe-events-abbr tribe-events-start-time published dtstart')]")
        
#         event_name.append(RawEventName)
#         event_desc.append(RawEventDesc)
#         event_date.append(RawEventDate)
#         event_time.append(RawEventTime)

#     newLink = tryXPATH(driver,False,True,"//a[contains(@rel, 'next')]",'href')
#     if newLink == '':
#         break
#     else:
#         driver.get(newLink)

        
# driver.get('https://zicklin.baruch.cuny.edu/')
           
# university_name = tryXPATH(driver,False,True,"//title",'textContent')

# university_contact_info = tryXPATH(driver,False,False,"//a[contains(@class ,'phone')]")

# for i in range(len(event_name)):
#     print(university_name)
#     print(university_contact_info)
#     print(logo)
#     print(event_name[i])
#     print(event_desc[i])
#     print(event_date[i])
#     print(event_time[i])