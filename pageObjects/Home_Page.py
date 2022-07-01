import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.readProperties import readConfig


class HomePage:
    URL = readConfig.getApplicationURL()
    search_engine_text_field_id = 'search_query_top'
    search_engine_button_XPath = '//*[@id="searchbox"]/button'
    contact_us_link_id = 'contact-link'
    sign_inButton_XPath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    e_mail_address_ID = 'email_create'
    submit_button_ID = 'SubmitCreate'
    registered_e_mail_ID = 'email'
    registered_password_ID = 'passwd'
    Sign_In_button = 'SubmitLogin'
    message_field = 'message'
    send_button_ID = 'submitMessage'
    home_back_button_XPATH = '//*[@id="center_column"]/ul/li/a'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_homePage(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def setSearchEngine_textfield(self, searched_text):
        self.driver.find_element(By.ID, self.search_engine_text_field_id).send_keys(searched_text)

    def searchEngine_click_button(self):
        self.driver.find_element(By.XPATH, self.search_engine_button_XPath).click()

    def contact_us_link(self):
        self.driver.find_element(By.ID, self.contact_us_link_id).click()

    def create_an_account(self, e_mail):
        self.driver.find_element(By.XPATH, self.sign_inButton_XPath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.e_mail_address_ID).click()
        self.driver.find_element(By.ID, self.e_mail_address_ID).send_keys(e_mail)
        self.driver.find_element(By.ID, self.submit_button_ID).click()
        time.sleep(3)

    def registration_form(self):
        self.driver.find_element(By.ID, 'id_gender1').click()
        self.driver.find_element(By.ID, 'customer_firstname').send_keys('Plamen')
        self.driver.find_element(By.ID, 'customer_lastname').send_keys('Petrov')
        self.driver.execute_script('window.scrollBy(0,500)' "")
        self.driver.find_element(By.ID, 'passwd').send_keys('12345')
        dropdown = Select(self.driver.find_element(By.ID, 'days'))
        time.sleep(2)
        dropdown.select_by_value('15')
        dropdown1 = Select(self.driver.find_element(By.ID, 'months'))
        dropdown1.select_by_value('4')
        dropdown2 = Select(self.driver.find_element(By.ID, 'years'))
        dropdown2.select_by_value('1987')
        self.driver.find_element(By.ID, 'uniform-newsletter').click()
        self.driver.find_element(By.ID, 'optin').click()
        self.driver.execute_script('window.scrollBy(0,800)' "")
        self.driver.find_element(By.ID, 'address1').send_keys('Mladost 1 A, bl.345')
        self.driver.find_element(By.ID, 'city').send_keys('Sofia')
        dropdown3 = Select(self.driver.find_element(By.ID, 'id_state'))
        dropdown3.select_by_value('7')
        self.driver.find_element(By.ID, 'postcode').send_keys('00000')
        self.driver.find_element(By.ID, 'other').send_keys('Am i here')
        self.driver.find_element(By.ID, 'phone_mobile').send_keys('088885252365')
        self.driver.find_element(By.ID, 'alias').send_keys('Same address')
        self.driver.find_element(By.ID, 'submitAccount').click()

    def sign_in(self, e_mail, password):
        self.driver.find_element(By.XPATH, self.sign_inButton_XPath).click()
        self.driver.find_element(By.ID, self.registered_e_mail_ID).send_keys(e_mail)
        self.driver.find_element(By.ID, self.registered_password_ID).send_keys(password)
        self.driver.find_element(By.ID, self.Sign_In_button).click()
        self.driver.find_element(By.XPATH, self.home_back_button_XPATH).click()

    def contactUs_functionality(self, message):
        self.driver.find_element(By.ID, self.contact_us_link_id).click()
        dropdown = Select(self.driver.find_element(By.ID, 'id_contact'))
        dropdown.select_by_value('1')
        self.driver.find_element(By.ID, self.message_field).send_keys(message)
        self.driver.find_element(By.ID, self.send_button_ID).click()






