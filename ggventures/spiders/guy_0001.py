import scrapy, time
# from scrapy import Selector
from datetime import datetime

from bot_email import missing_info_email, error_email, unique_event, website_changed

from binaries import Load_Driver, logger, WebScroller, EventBrite_API

from scrapy.loader import ItemLoader

from ggventures.items import GgventuresItem

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Guy0001Spider(scrapy.Spider):
    name = 'guy_0001'
    # allowed_domains = ['https://fss.uog.edu.gy/']
    start_urls = ['https://fss.uog.edu.gy/']
    country = 'Guyana'
    # handle_httpstatus_list = [403,404]
    # eventbrite_id = 13656989385

    def __init__(self):
        self.driver = Load_Driver()
        self.getter = Load_Driver()
        # self.eventbrite_api = EventBrite_API()
        self.start_time = round(time.time())
        self.scrape_time = None

    def parse(self, response):
        try:
            # EVENTBRITE API - ORGANIZATION REQUEST
            # raw_org = self.eventbrite_api.get_organizers(self.eventbrite_id)
            #
            # university_name = raw_org['name']
            # if raw_org['logo']:
            #     logo = raw_org['logo']['url']
            # else:
            #     logo = 'https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/opmvsxxxncnsbevwjn1a'

            # if not logo:
            #     logo = (WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,"//img[contains(@class, 'vert')]")))).get_attribute('src')


            self.driver.get(response.url)
            university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class,'data-list')]")))).text
            university_name = 'University of Guyana,Faculty of Social Sciences'
            # university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH, "//p[contains(@class,'telephone')]/span")))).get_attribute('textContent')
            logo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwoL1dh43_cpgpTEtCEbV41pqt64boaq-o3w&usqp=CAU'

            # EVENTBRITE API - EVENT LIST REQUEST
            # raw_event = self.eventbrite_api.get_organizer_events(self.eventbrite_id)
            # last_page = int(raw_event['pagination']['page_count'])
            # prev_last_page = int(raw_event['pagination']['page_count']) - 1
            #
            # event_list = self.eventbrite_api.get_organizer_events(self.eventbrite_id,page=prev_last_page)['events'] + self.eventbrite_api.get_organizer_events(self.eventbrite_id,page=last_page)['events']
            #
            # for event in event_list:
            #     if datetime.strptime(event['start']['utc'].split('T')[0],'%Y-%m-%d') > datetime.utcnow():
            #         data = ItemLoader(item = GgventuresItem(), selector = event)
            #         data.add_value('university_name',university_name)
            #         data.add_value('university_contact_info',university_contact_info)
            #         data.add_value('logo',logo)
            #         data.add_value('event_name', event['name']['text'])
            #         data.add_value('event_desc', event['description']['text'])
            #         data.add_value('event_date', f"Start Date: {event['start']['utc']} - End Date: {event['end']['utc']}")
            #         data.add_value('event_link', event['url'])
            #         # data.add_value('event_time', event_time[i])
            #         yield data.load_item()

            self.driver.get("https://fss.uog.edu.gy/upcoming-events")

            ############### NO EVENTS CODE #########################

            try:
                no_events = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'region-content') and string-length(text()) > 5]")))
            except (TimeoutException,NoSuchElementException) as e:
                no_events = ''

            # no_events = self.driver.find_element(By.XPATH, "//li[contains(text(),'No upcoming')]")

            if no_events:
                logger.debug('Changes to Events on current Spider. Sending emails....')
                website_changed(self.name,university_name)
            else:
                logger.debug('No changes to Events on current Spider. Skipping.....')

            ########################################################

            # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'Coming-year')]"))).click()
            #
            # time.sleep(10)

            # counter = 0
            # while True:
            #     try:
            #         LoadMore = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'cal_load-button')]/button"))).click()
            #         logger.info("Load More Events....")
            #         time.sleep(10)
            #         counter+=1
            #         if counter >= 10:
            #             logger.debug(f"Loaded all Events. Start Scraping......")
            #             break
            #     except TimeoutException as e:
            #         logger.debug(f"No more Events to load --> {e}. Start Scraping......")
            #         break
            #
            # time.sleep(20)

            # EventLinks = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//h2[contains(@class,'cal_calendar-item')]/a")))
            #
            # for i in EventLinks:
            #
            #     data = ItemLoader(item = GgventuresItem(), selector = i)
            #
            #     link = i.get_attribute('href')
            #     self.getter.get(link)
            #
            #     # if 'www.hec.ca/en/programs' in self.getter.current_url:
            #
            #     logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #     # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail')]")))
            #
            #     # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail')]"))
            #
            #     data.add_value('university_name',university_name)
            #     data.add_value('university_contact_info',university_contact_info)
            #     data.add_value('logo',logo)
            #     data.add_value('event_name', WebDriverWait(self.getter,120).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'primary-header')]"))).text)
            #     # data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1"))).get_attribute('textContent'))
            #     # data.add_value('event_name', i.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
            #
            #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//c-form-section_lwc[contains(@data-dragindex,'2')]/div").text)
            #     # data.add_value('event_desc', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//article/p")]))
            #
            #     # try:
            #     #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'InstAccueilContainer')]").text)
            #     # except NoSuchElementException as e:
            #     #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #     #     data.add_value('event_desc', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//div[contains(@class,'hEventStart')]/following-sibling::p[not(@id)]")]))
            #     # try:
            #     #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'details')]/div[contains(@class,'wrapper')]").text)
            #     # except NoSuchElementException as e:
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #
            #     # data.add_value('event_date', self.getter.find_element(By.XPATH,"//p[contains(@class,'fa-calendar')]/following-sibling::p").text)
            #     # data.add_value('event_time', self.getter.find_element(By.XPATH,"//p[contains(@class,'fa-clock')]/following-sibling::p").text)
            #
            #     data.add_value('event_date', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//lightning-formatted-text/parent::p")]) )
            #     data.add_value('event_time', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//lightning-formatted-text/parent::p")]) )
            #
            #     # try:
            #     #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//div[contains(@class,'hEventStart')]").text)
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//div[contains(@class,'hEventStart')]").text)
            #     # except NoSuchElementException as e:
            #     #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #     #     try:
            #     #         data.add_value('event_date', self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]/parent::span").text)
            #     #         data.add_value('event_time', self.getter.find_element(By.XPATH,"//strong[contains(text(),'Date')]/parent::span").text)
            #     #     except (TimeoutException,NoSuchElementException) as e:
            #     #         logger.debug(f"Element cannot be located --> {e}")
            #
            #     #
            #     # try:
            #     #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//strong[contains(text(),'Time')]/parent::p").text)
            #     # except NoSuchElementException as e:
            #     #     # logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #     #     try:
            #     #         data.add_value('event_time', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
            #     #     except (TimeoutException,NoSuchElementException) as e:
            #     #         logger.debug(f"Element cannot be located --> {e}")
            #
            #     # data.add_value('event_link', link)
            #     # try:
            #     #     # event_phone = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_phone_number')]"))).text
            #     #     event_phone =self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-tel')]").text
            #     # except (TimeoutException,NoSuchElementException) as e:
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #     #     event_phone = ''
            #     #
            #     # try:
            #     #     # event_email = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_email')]"))).text
            #     #     # event_email = self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-email')]").text
            #     #     event_email = self.getter.find_element(By.XPATH,"//a[contains(@class,'event-email')]").get_attribute('textContent')
            #     # except (TimeoutException,NoSuchElementException) as e:
            #     #     logger.debug(f"Element cannot be located --> {e}")
            #     #     event_email = ''
            #     # data.add_value('startups_contact_info', event_email+'\n'+event_phone)
            #     # data.add_value('startups_contact_info', '\n'.join([x.get_attribute('href') for x in self.getter.find_elements(By.XPATH,"//p[contains(@class,'fa-whatsapp')]/following-sibling::p//a")]))
            #     # data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,"//dd[contains(@class,'sys_events-contact')]").text)
            #
            #     data.add_value('event_link', link)
            #
            #
            #     yield data.load_item()
            #
            #     else:
            #         logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
            #         unique_event(self.name,university_name,self.getter.current_url)
            #         logger.debug("Skipping............")

            # number_of_months = 8
            # #
            # for scrape_month in range(number_of_months):
            #
            #     try:
            #         # time.sleep(10)
            #
            #         EventLinks = WebDriverWait(self.driver,25).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'ep-view-event')]")))
            #
            #         for i in EventLinks:
            #
            #             data = ItemLoader(item = GgventuresItem(), selector = i)
            #
            #             # self.getter.get(i.get_attribute('href'))
            #             # link = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//li[contains(@class,'e-url')]/a"))).get_attribute('href')
            #
            #             link = i.get_attribute('href')
            #             self.getter.get(link)
            #
            #             # if 'brunel.ac.uk/news-and-events/events' in self.getter.current_url:
            #
            #             logger.info(f"Currently scraping --> {self.getter.current_url}")
            #
            #             # WebDriverWait(self.getter,20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@title,'Event Detail')]")))
            #
            #             # self.getter.switch_to.frame(self.getter.find_element(By.XPATH,"//iframe[contains(@title,'Event Detail')]"))
            #
            #             data.add_value('university_name',university_name)
            #             data.add_value('university_contact_info',university_contact_info)
            #             data.add_value('logo',logo)
            #             data.add_value('event_name', WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h2[contains(@itemprop,'name')]"))).text)
            #             # data.add_value('event_name', i.find_element(By.XPATH,".//span[contains(@class,'event-title')]").text)
            #             data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@itemprop,'description')]").text)
            #             # data.add_value('event_desc', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//div[contains(@class,'about-description')]/*[not(self::aside)]")]))
            #             # try:
            #             #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@id,'content-info')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             #     data.add_value('event_desc', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//section[contains(@aria-label,'Event information')]/p")]))
            #             # try:
            #             #     data.add_value('event_desc', self.getter.find_element(By.XPATH,"//div[contains(@class,'details')]/div[contains(@class,'wrapper')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Element cannot be located --> {e}")
            #
            #             data.add_value('event_date', self.getter.find_element(By.XPATH,"//section[contains(@class,'event-detail-date')]").text)
            #             data.add_value('event_time', self.getter.find_element(By.XPATH,"//section[contains(@class,'event-detail-date')]").text)
            #
            #             # try:
            #             #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//div[contains(@class,'event-instance')]").text)
            #             #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//div[contains(@class,'event-instance')]").text)
            #             # except (TimeoutException,NoSuchElementException) as e:
            #             #     logger.debug(f"Element 'event_date/event_time' cannot be located --> {e}")
            #
            #             # data.add_value('event_date', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//span[contains(text(),'Calendar')]/parent::dt/following-sibling::dd")]) )
            #             # data.add_value('event_time', '\n'.join([x.text for x in self.getter.find_elements(By.XPATH,"//span[contains(text(),'Clock')]/parent::dt/following-sibling::dd")]) )
            #
            #             # try:
            #             #     data.add_value('event_date', self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text)
            #             #     # data.add_value('event_time', self.getter.find_element(By.XPATH,"//span[contains(@class,'date-display-single')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             #     try:
            #             #         data.add_value('event_date', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
            #             #     except (TimeoutException,NoSuchElementException) as e:
            #             #         logger.debug(f"Element cannot be located --> {e}")
            #             #
            #             #
            #             # try:
            #             #     data.add_value('event_time', self.getter.find_element(By.XPATH,"//div[contains(@class,'date')]").text)
            #             # except NoSuchElementException as e:
            #             #     logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
            #             #     try:
            #             #         data.add_value('event_time', self.getter.find_element(By.XPATH,"//ul[contains(@class,'date-recur-occurrences')]").text)
            #             #     except (TimeoutException,NoSuchElementException) as e:
            #             #         logger.debug(f"Element cannot be located --> {e}")
            #
            #             # data.add_value('event_link', link)
            #             # try:
            #                 # event_phone = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_phone_number')]"))).text
            #             #     event_phone =self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-tel')]").text
            #             # except (TimeoutException,NoSuchElementException) as e:
            #             #     logger.debug(f"Element cannot be located --> {e}")
            #             #     event_phone = ''
            #
            #             # try:
            #             #     # event_email = WebDriverWait(self.getter,5).until(EC.presence_of_element_located((By.XPATH,"//dd[contains(@class,'contact_email')]"))).text
            #             #     # event_email = self.getter.find_element(By.XPATH,"//dd[contains(@class,'tribe-organizer-email')]").text
            #             #     event_email = self.getter.find_element(By.XPATH,"//a[contains(@class,'event-email')]").get_attribute('textContent')
            #             # except (TimeoutException,NoSuchElementException) as e:
            #             #     logger.debug(f"Element cannot be located --> {e}")
            #             #     event_email = ''
            #             # data.add_value('startups_contact_info', event_email+'\n'+event_phone)
            #             # data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,"//aside[contains(@class,'layout-sidebar-second')]").text)
            #             # try:
            #             #     data.add_value('startups_contact_info', self.getter.find_element(By.XPATH,"//div[contains(@id,'evenement-contact')]").text)
            #             # except (TimeoutException,NoSuchElementException) as e:
            #             #     logger.debug(f"Element 'startups_contact_info' cannot be located --> {e}")
            #
            #             data.add_value('event_link', link)
            #
            #
            #             yield data.load_item()
            #
            #             # else:
            #             #     logger.debug(f"Link: {self.getter.current_url} is a Unique Event. Sending Emails.....")
            #             #     unique_event(self.name,university_name,self.getter.current_url)
            #             #     logger.debug("Skipping............")
            #
            #     except TimeoutException as e:
            #         logger.debug(f"No available events for this month : {e} ---> Skipping...........")
            #
            #
            #     try:
            #         # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'next-btn')]"))).click()
            #         # next_month = self.driver.find_element(By.XPATH,"//a[contains(@id,'view_by_next')]").get_attribute('href')
            #         # next_month = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'Go to the next page of the results')]"))).get_attribute('href')
            #         WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@id,'view_by_next')]"))).click()
            #         # self.driver.get(next_month)
            #         # self.driver.execute_script(f"""return document.querySelector("[onclick*={next_month.split('(')[1].split(')')[0]}]")""").click()
            #         # time.sleep(10)
            #     except (TimeoutException,NoSuchElementException) as e:
            #         logger.debug(f"Experienced Timeout Error on Spider: {self.name} --> {e}. Moving to the next spider...")
            #         break

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
