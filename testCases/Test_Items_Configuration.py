import time
from selenium.webdriver.common.by import By
from pageObjects.Home_Page import HomePage
from pageObjects.Items_Configuration import Items
from utilities.readProperties import readConfig


class Test_02_Items_Configuration:
    e_mail = readConfig.getUserEmail()
    password = readConfig.getPassword()

    def test_women_tShirt_configuration(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        time.sleep(3)
        self.ic = Items(self.driver)
        self.ic.women_tShirt_configuration()
        result = self.driver.find_element(By.CSS_SELECTOR, "#center_column > div > div > "
                                                           "div.pb-center-column.col-xs-12.col-sm-4 > h1").text
        assert "Faded Short Sleeve T-shirts" in result
        self.driver.close()

    def test_women_blouses_configuration(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        time.sleep(3)
        self.ic = Items(self.driver)
        self.ic.women_blouses_configuration()
        result = self.driver.find_element(By.XPATH, '//*[@id="short_description_content"]').text
        assert "Short sleeved blouse with feminine draped sleeve detail." in result
        self.driver.close()

    def test_sell_items(self, setup):
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.load_homePage()
        self.hp.sign_in(self.e_mail, self.password)
        time.sleep(3)
        self.ic = Items(self.driver)
        self.ic.sell_items()
        result = self.driver.find_element(By.CSS_SELECTOR, '#cart_title > span').text
        assert "Your shopping cart contains:" in result


