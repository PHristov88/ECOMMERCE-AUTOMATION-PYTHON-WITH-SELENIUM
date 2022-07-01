import time
from selenium.webdriver.common.by import By
from pageObjects.Home_Page import HomePage
from utilities.readProperties import readConfig


class Test_01_Home_Page:
    URL = readConfig.getApplicationURL()
    e_mail = readConfig.getUserEmail()
    search_engine_text = readConfig.getSearchedText()
    password = readConfig.getPassword()
    message = readConfig.getMessage()

    def test_search_engine(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        self.hp.setSearchEngine_textfield(self.search_engine_text)
        self.hp.searchEngine_click_button()
        time.sleep(2)
        result = self.driver.find_element(By.CSS_SELECTOR,
                                          '#center_column > ul > li > div > div.right-block > h5 > a').text

        assert 'T-shirt' in result
        self.driver.close()

    def test_registration(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        self.hp.create_an_account(self.e_mail)
        time.sleep(2)
        self.hp.registration_form()
        result = self.driver.find_element(By.CSS_SELECTOR, '#center_column').text
        if 'Welcome to your account' in result:
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_registration.png')
            assert False
        self.driver.close()

    def test_signIn(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        time.sleep(3)
        self.hp.sign_in(self.e_mail, self.password)
        result = self.driver.find_element(By.CSS_SELECTOR, '#center_column').text
        if 'Welcome to your account' in result:
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_registration_error.png')
            self.driver.close()
            assert False
        self.driver.close()

    def test_contactUs(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        time.sleep(2)
        self.hp.sign_in(self.e_mail, self.password)
        self.hp.contactUs_functionality(self.message)
        time.sleep(2)
        result = self.driver.find_element(By.CSS_SELECTOR, '#center_column > p').text
        if 'Your message has been successfully sent to our team.' in result:
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_contactUs_functionality_error.png')
            self.driver.close()
            assert False
        self.driver.close()




