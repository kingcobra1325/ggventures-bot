import scrapy


class Usa0028Spider(scrapy.Spider):
    name = 'usa_0028'
    start_urls = ['https://www.fdu.edu/academics/colleges-schools/silberman/']
    country = 'US'

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            # event_name = list()
            # event_date = list()
            # event_time = list()
            # event_desc = list()
            # event_link = list()

            self.driver.get(response.url)

            logo = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@class,'brand-logo')]"))).get_attribute("src")

            university_name = 'Fairleigh Dickinson University, Silberman College of Business'

            self.driver.get("https://www.fdu.edu/about/contact-us/")

            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Contacts')]/parent::div")))).text

            self.driver.get(response.url)

            select = Select(WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'jump_menu')]"))))
            select.select_by_value('all')

            time.sleep(4)

            EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@title,'Expand to View')]")))

            for i in EventLinks:
                self.getter.get(i.get_attribute('href'))

                if 'gsb.columbia.edu' in i.get_attribute('href'):

                    data = ItemLoader(item = GgventuresItem(), selector = i)
                    data.add_value('university_name',university_name)
                    data.add_value('university_contact_info',university_contact_info)
                    data.add_value('logo',logo)
                    data.add_value('event_name', WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH, "//h1"))).text)
                    data.add_value('event_desc', self.getter.find_elements(By.XPATH , "//div[contains(@class,'col-md-4_5')]//p")[0].text)
                    data.add_value('event_date', self.getter.find_elements(By.XPATH , "//div[contains(@class,'col-md-4_5')]//p")[1].text)
                    data.add_value('event_time', self.getter.find_element(By.XPATH , "//div[contains(@id,'event_details')]").text)
                    data.add_value('event_link', i.get_attribute('href'))

                    yield data.load_item()
                else:
                    logger.debug(f"Link: {i.get_attribute('href')} is a Unique Event. Sending Emails.....")
                    unique_event(self.name,university_name,i.get_attribute('href'))
                    logger.debug("Skipping............")


        except Exception as e:
            logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
    def closed(self, reason):
        try:
            self.driver.quit()
            self.getter.quit()
            self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
            logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
            logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
        except Exception as e:
            logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
            error_email(self.name,e)
