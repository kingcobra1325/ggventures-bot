# if __name__ == '__main__':
#     from time import sleep

#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     def tryXPATH(driver,isList,isFirst,tempPath,hasAttrib = None):
#         try:
#             if isList and isFirst:
#                 return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,tempPath)))
#             elif isList:
#                 return driver.find_elements(By.XPATH,tempPath)
#             elif not isList and hasAttrib and isFirst:
#                 return (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,tempPath)))).get_attribute(hasAttrib)
#             elif not isList and isFirst:
#                 return (WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,tempPath)))).text
#             else:
#                 return driver.find_element(By.XPATH,tempPath).text
#         except Exception as e:
#             print(e)
#             #logger.error()
#             return ''


#     link = "https://calendar.auburn.edu/calendar"

#     options = webdriver.ChromeOptions()
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
#     options.add_argument(f'user-agent={user_agent}')
#     # options.add_argument('--headless')
#     options.add_argument('--log-level 3') 
#     driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
#     getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
#     driver.get(link)
#     height = driver.execute_script("return document.body.scrollHeight")

#     logo = tryXPATH(driver,False,True,"//img[contains(@alt, 'Auburn University homepage') and contains(@class, 'hidden-print')]",'src')

#     for i in range(1,height,int(height/5)):
#         driver.execute_script("window.scrollBy(0, {0});".format(i))
#         sleep(0.5)
        
#     EventLinks = tryXPATH(driver,True,True,"//h3/a")

#     event_name = list()
#     event_date = list()
#     event_time = list()
#     event_desc = list()

#     for i in EventLinks:
#         getter.get(i.get_attribute('href'))
        
#         RawEventName = tryXPATH(getter,False,True,"//h1[contains(@class ,'em-header-card_title')]")
        
#         RawEventDesc = tryXPATH(getter,False,False,"//div[starts-with(@class, 'em-content_about')]")
        
#         RawEventDate = tryXPATH(getter,False,False,"//p[contains(@class, 'em-date')]")
        
#         #Some Events have time embedded in Date
#         #RawEventTime = tryXPATH(getter,False,False,"//div[contains(@class,'view-content')]/div/p/br")
        
#         event_name.append(RawEventName)
#         event_desc.append(RawEventDesc)
#         event_date.append(RawEventDate)
#         #event_time.append(RawEventTime)

#     university_contact_info = tryXPATH(driver,False,True,"//div[contains(@class, 'col-xs-6')]")

#     driver.get('https://www.auburn.edu/')

#     university_name = tryXPATH(driver,False,True,"//title",'textContent')

#     for i in range(len(EventLinks)):
#         print(university_name)
#         print(university_contact_info)
#         print(logo)
#         print(event_name[i])
#         print(event_desc[i])
#         print(event_date[i])
#         #print(event_time[i])


