from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.readProperties import readConfig
from selenium.webdriver import ActionChains
import time


class Items:
    l_size_ID = 'layered_id_attribute_group_3'
    blue_color_ID = 'layered_id_attribute_group_14'
    compositions_cotton_ID = "layered_id_feature_5"
    style_casual_ID = 'layered_id_feature_11'
    item_quick_view_Link_text = "Faded Short Sleeve T-shirts "
    blouses_size_ID = "layered_id_attribute_group_1"
    blouses_color_ID = "layered_id_attribute_group_11"
    blouses_compositions_ID = "layered_id_feature_5"
    blouses_styles_ID = "uniform-layered_id_feature_11"
    continue_shopping_Xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span'
    cart_CSS = "#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a"
    proceed_to_checkout_Xpath = '//*[@id="center_column"]/p[2]/a[1]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def women_tShirt_configuration(self):
        women = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
        t_shirt = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[1]/a')
        action = ActionChains(self.driver)
        action.move_to_element(women).move_to_element(t_shirt).click().perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.l_size_ID).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.blue_color_ID).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.compositions_cotton_ID).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.style_casual_ID).click()
        self.driver.implicitly_wait(60)
        self.driver.execute_script('window.scrollBy(0, 400)', "")
        quick_view = self.driver.find_element(By.LINK_TEXT, "Faded Short Sleeve T-shirts")
        action.move_to_element(quick_view).click().perform()

    def women_blouses_configuration(self):
        women = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
        blouses = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[2]/a')
        action = ActionChains(self.driver)
        action.move_to_element(women).move_to_element(blouses).click().perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.blouses_size_ID).click()
        self.driver.find_element(By.ID, self.blouses_color_ID).click()
        self.driver.find_element(By.ID, self.blouses_compositions_ID).click()
        self.driver.find_element(By.ID, self.blouses_styles_ID).click()
        self.driver.execute_script('window.scrollBy(0, 400)', "")
        self.driver.implicitly_wait(120)
        quick_view = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div')
        white_color = self.driver.find_element(By.ID, 'color_8')
        action.move_to_element(quick_view).move_to_element(white_color).click().perform()
        self.driver.execute_script('window.scrollBy(0, 400)', "")
        self.driver.find_element(By.XPATH, '//*[@id="bigpic"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="product"]/div[2]/div/a').click()

    def sell_items(self):
        self.driver.execute_script('window.scrollBy(0,400)', "")
        t_shirt = self.driver.find_element(By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img')
        add_toCart_button = self.driver.find_element(By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]')
        action = ActionChains(self.driver)
        action.move_to_element(t_shirt).move_to_element(add_toCart_button).click().perform()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, self.continue_shopping_Xpath).click()
        blouse = self.driver.find_element(By.XPATH, '//*[@id="homefeatured"]/li[2]/div')
        add_toCart_button2 = self.driver.find_element(By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a['
                                                                '1]/span')
        action.move_to_element(blouse).move_to_element(add_toCart_button2).click().perform()
        self.driver.find_element(By.XPATH, self.continue_shopping_Xpath).click()
        self.driver.execute_script('window.scrollBy(400,0)', "")
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a').click()
        self.driver.execute_script('window.scrollBy(0, 400)', "")
        self.driver.find_element(By.XPATH, self.proceed_to_checkout_Xpath).click()