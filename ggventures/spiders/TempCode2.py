# if __name__ == '__main__':
#     from time import sleep

#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     link = "https://www.babson.edu/about/news-events/babson-events/"

#     options = webdriver.ChromeOptions()
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
#     options.add_argument(f'user-agent={user_agent}')
#     # options.add_argument('--headless')
#     options.add_argument('--log-level 3') 
#     driver = webdriver.Chrome(executable_path='C:\Chromium\chromedriver',options=options)
#     driver.get(link)
#     height = driver.execute_script("return document.body.scrollHeight")

#     event_name = list()
#     event_date = list()
#     event_time = list()
#     event_desc = list()


#     logo = None
#     # logo draw
#     for i in range(1,height,int(height/5)):
#         driver.execute_script("window.scrollBy(0, {0});".format(i))
#         sleep(0.5)
        

#     for i in range(3):
#         EventLinks = WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//li[contains(@class, 'event-item snippet event clearfix')]")))
#         for o in EventLinks:
#             event_name.append(o.find_element(By.XPATH,".//div[contains(@class, 'event-info')]/header").text.strip())
#             event_desc.append(o.find_element(By.XPATH, ".//div[starts-with(@class, 'image')]").get_attribute('textContent').strip())
#             event_date.append(o.find_element(By.XPATH, ".//div[contains(@class, 'event-date-box')]").text.strip())
#             event_time.append(o.find_element(By.XPATH, "//p[contains(@class, 'categories_trigger ajax-load-link')]").text.strip())
#         Next_Link = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 'next-search-link')]")))).get_attribute('href')
#         driver.get(Next_Link)
#         print(event_name)

#     university_name = (WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH , "//div[contains(@class,'header__logo')]/a")))).get_attribute('title')

#     university_contact_info = driver.find_element(By.XPATH,"//div[contains(@class, 'footer-addy')]/a[starts-with(@target, '_blank')]").text
        
#     for i in range(len(event_name)):
#         print(university_name)
#         print(university_contact_info)
#         print(logo)
#         print(event_name[i])
#         print(event_desc[i])
#         print(event_date[i])
#         print(event_time[i])