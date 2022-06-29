if __name__ == '__main__':
    from time import sleep

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
    
    import re

    options = webdriver.ChromeOptions()
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    # options.add_argument(f'user-agent={user_agent}')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_argument('--log-level 3') 
    driver = webdriver.Chrome(executable_path='C:\Chromium97\chromedriver',options=options)
    # getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
    # getter2 = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
    
    link = "https://www.santelmo.org/agenda"
    myList = []
    driver.get(link)
    base_site = "https://www.santelmo.org"
    new_list = []
    try:
        WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='event-button']/button")))
        myList.extend([x.get_attribute('onclick') for x in driver.find_elements(By.XPATH,"//div[@class='event-button']/button")])
        for i in myList:
            regexlink = re.search('href="\/\S+"',i).group()
            regexnew= regexlink.replace('href=','').replace('\"','')
            new_list.append(f'{base_site}{regexnew}')
        # print(new_list)
    except Exception as e:
        print(e)
    # driver.maximize_window()
    # EventLinks = WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='twMonthEventContainer']//a")))
    # for i in EventLinks:
    #     driver.get(i.get_attribute('href'))
        
    sleep(100)

    



    # Logo = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//h2/a")))).value_of_css_property("background")
    # Logo = re.findall(r'''\"(\S+)\"''',Logo)[0]
    
    # print(Logo)

        
        # for i in EventLinks:
        #     getter.get(i.get_attribute('href'))
                
        #     RawEventName = (WebDriverWait(getter,60).until(EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'heading__light')]")))).text
            
        #     RawEventDesc = getter.find_element(By.XPATH,"//div[contains(@class,'wysiwyg-container')]").text

        #     RawEventDate = getter.find_element(By.XPATH,"//div[contains(@class,'event-card__date--inner')]").text
            
        #     try:
        #         RawEventTime = getter.find_element(By.XPATH,"//div[contains(@class,'event__label--wrapper')]/span[2]").text
        #     except:
        #         RawEventTime = None
        #     print(RawEventName)
        
        
    # for o in range(3):
    #     Element = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//li[contains(@class,'school-drucker-school-of-management')]/input"))))
    #     driver.execute_script("arguments[0].scrollIntoView();", Element)
    #     Element.click()
    #     sleep(3)
    #     TestLinks = driver.find_elements(By.XPATH,"//a[contains(@class,'event__url')]")
    #     print(len(TestLinks))
    #     Links = driver.find_elements(By.XPATH,"//a[contains(@class,'event__url')]")
    #     for i in Links:
    #         print(i.text) 
    #     driver.get(driver.find_element(By.XPATH,"//a[contains(@rel,'next')]").get_attribute('href'))
    # sleep(100)
    # for i in EventLinks:
    #     print(i.get_attribute('href'))
    
    # EventLinks = WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'items-scroller')]/div")))

    # Stop = driver.find_element(By.XPATH, "//div[contains(@title,'Pause')]")
    # Stop.click()
    
    # for i in EventLinks:
    #     i.click()
               
    #     EventPopUp = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'six columns scroller-text')]/h1")))
        
    #     EventPopUp.click()
        
    #     RawEventName = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'row pl10 pr20')]/h2")))).text
               
    #     RawEventDesc =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[starts-with(@id, 'eventDescriptionEventDetails')]")))).text
        
    #     RawEventDate =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'row pl10 pr20')]//div[contains(@class,'info-date')]")))).text
        
    #     RawEventTime =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'row pl10 pr20')]//div[contains(@class,'info-time fl')]")))).text
        
    #     RawEventLink =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'row pl10 pr20')]//div[contains(@class,'font-weight-normal')])[3]")))).text

    #     PopClose = driver.find_element(By.XPATH, "//a[contains(@title,'Close')]").click()
        
    #     try:
    #         driver.find_element(By.XPATH, "//div[contains(@class,'prev-next pointer next-item')]").click()
    #     except:
    #         break
        
        
    #     print(RawEventName)
    #     print(RawEventDesc)
    #     print(RawEventDate)
    #     print(RawEventTime)
    #     print(RawEventLink)
        
        
        