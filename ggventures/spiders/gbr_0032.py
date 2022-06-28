from spider_template import GGVenturesSpider

# class (scrapy.Spider):
#     name = 'gbr_0032'
#     country = 'United Kingdom'
#     # start_urls = ["https://cba.k-state.edu/about/events/"]
#     start_urls = ["https://www.jbs.cam.ac.uk/insight/events/"]

#     def __init__(self):
#         self.driver = Load_Driver()
#         self.getter = Load_Driver()
#         self.start_time = round(time.time())
#         self.scrape_time = None

#     def parse(self, response):
#         try:
#             self.driver.get("https://www.jbs.cam.ac.uk/")

#             logo = "https://www.jbs.cam.ac.uk/wp-content/uploads/2019/11/judge-logo-small.png"
#             # logo = re.findall(r'''\"(\S+)\"''',logo)[0]

#             university_name = 
            
#             self.driver.get("")
            
#             university_contact_info = (WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,"//h2[text()='General enquiries']/..")))).text

#             self.driver.get(response.url)     
            
#             counter = 0
#             for o in range(3):
#                 EventLinks = WebDriverWait(self.driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@title='name']")))
#                 for i in EventLinks:
#                     self.getter.get(i.get_attribute('href'))

#                     RawEventName = (WebDriverWait(self.getter,60).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='campl-sub-title']")))).text
#                     RawEventDesc = ""
#                     try:
#                         RawPs = self.getter.find_elements(By.XPATH,"//div[@id='espresso-event-details-dv']/p")
#                         for x in RawPs:
#                             RawEventDesc += x.text + '\n'
#                     except:
#                         RawEventDesc = None

#                     try:
#                         RawEventDate = self.getter.find_element(By.XPATH,"//span[@class='span_event_date_value']").text
#                     except:
#                         RawEventDate = None
                        
#                     try:
#                         # RawEventTime = None                    
#                         RawEventTime = self.getter.find_element(By.XPATH,"//p[@class='start_date']").text 
#                         # RawEventTime = RawEventDate
#                     except:
#                         RawEventTime = None
                        
#                     # try:
#                     #     RawStartContactInfo = self.getter.find_element(By.XPATH,"//dt[text()='Contact']/..").text
#                     # except:
#                     #     RawStartContactInfo = None

#                     data = ItemLoader(item = GgventuresItem(), selector = counter)
#                     data.add_value('university_name',university_name)
#                     data.add_value('university_contact_info',university_contact_info)
#                     data.add_value('logo',logo)
#                     data.add_value('event_name', RawEventName)
#                     data.add_value('event_desc', RawEventDesc)
#                     data.add_value('event_date', RawEventDate)
#                     data.add_value('event_time', RawEventTime)
#                     data.add_value('event_link', i.get_attribute('href'))
#                     # data.add_value('startups_contact_info', RawStartContactInfo)
#                     counter+=1

#                     yield data.load_item()
#                 self.driver.get(self.driver.find_element(By.XPATH,"//a[contains(@class,'next')]").get_attribute('href'))

#         except Exception as e:
#             logger.error(f"Experienced error on Spider: {self.name} --> {e}. Sending Error Email Notification")
#             error_email(self.name,e)
#     def closed(self, reason):
#         try:
#             self.driver.quit()
#             self.getter.quit()
#             self.scrape_time = str(round(((time.time() - self.start_time) / float(60)), 2)) + ' minutes' if (time.time() - self.start_time > 60.0) else str(round(time.time() - self.start_time)) + ' seconds'
#             logger.debug(f"Spider: {self.name} scraping finished due to --> {reason}")
#             logger.debug(f"Elapsed Scraping Time: {self.scrape_time}")
#         except Exception as e:
#             logger.error(f"Experienced error while closing Spider: {self.name} with reason: {reason} --> {e}. Sending Error Email Notification")
#             error_email(self.name,e)

class Gbr0032Spider(GGVenturesSpider):
    name = 'gbr_0032'
    country = 'United Kingdom'
    # start_urls = ["https://cba.k-state.edu/about/events/"]
    start_urls = ["https://www.jbs.cam.ac.uk/aboutus/contact/"]
    # eventbrite_id = 14858065474
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "University of Cambridge,Judge Business School"
    static_logo = "https://www.rotman.utoronto.ca/-/media/Images/Central/MarketingResources/Rotman-Crest--blackfor-White-backgrounds.png?h=123&w=400&la=en&hash=C7E75A47C12A73AD2C6F148A4EB6C517A55F30A0"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.jbs.cam.ac.uk/insight/events/"

    university_contact_info_xpath = "//div[contains(@role,'contentinfo')]//td[1]"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//div[contains(@class,'cal_load-button')]/button",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[text()='>>']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@data-post-types='event']//h3/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['utoronto.ca/event']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'wp-block-column--content')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'wp-block-ob-blocks-post-metadata')]"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'wp-block-ob-blocks-post-metadata')]"],method='attr')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)