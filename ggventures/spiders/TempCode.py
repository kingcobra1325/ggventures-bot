if __name__ == '__main__':
    from time import sleep

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
        
    link = "http://specialevents.csulb.edu/mastercalendar/MasterCalendar.aspx"

    event_name = list()
    event_date = list()
    event_time = list()
    event_desc = list()

    options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--headless')
    options.add_argument('--log-level 3') 
    driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
    # getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
    driver.get(link)
    height = driver.execute_script("return document.body.scrollHeight")
    
    EventLinks = WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'items-scroller')]/div")))

    Stop = driver.find_element(By.XPATH, "//div[contains(@title,'Pause')]")
    Stop.click()
    
    for i in EventLinks:
        i.click()
               
        EventPopUp = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'six columns scroller-text')]/h1")))
        
        EventPopUp.click()
        
        RawEventName = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'row pl10 pr20')]/h2")))).text
               
        RawEventDesc =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[starts-with(@id, 'eventDescriptionEventDetails')]")))).text
        
        RawEventDate =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'row pl10 pr20')]//div[contains(@class,'info-date')]")))).text
        
        RawEventTime =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'row pl10 pr20')]//div[contains(@class,'info-time fl')]")))).text
        
        RawEventLink =  (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'row pl10 pr20')]//div[contains(@class,'font-weight-normal')])[3]")))).text

        PopClose = driver.find_element(By.XPATH, "//a[contains(@title,'Close')]").click()
        
        try:
            driver.find_element(By.XPATH, "//div[contains(@class,'prev-next pointer next-item')]").click()
        except:
            break
        
        
        print(RawEventName)
        print(RawEventDesc)
        print(RawEventDate)
        print(RawEventTime)
        print(RawEventLink)
        
        
        