if __name__ == '__main__':
    from time import sleep

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
        
    link = "https://www.baylor.edu/business/news/index.php?id=86163%27"

    event_name = list()
    event_date = list()
    event_time = list()
    event_desc = list()

    options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    # options.add_argument('--headless')
    options.add_argument('--log-level 3') 
    driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
    # getter = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
    driver.get(link)
    height = driver.execute_script("return document.body.scrollHeight")
    
    FirstElement = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@id, 'copyright')]/p")))).text.split('\n')[1]
    # TestElement = FirstElement.find_elements(By.XPATH,".//span[contains(@class,'datelisting')]")
    print(FirstElement)