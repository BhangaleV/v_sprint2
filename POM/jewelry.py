from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from Library.config import Config
from Data.reading_objects import LBehave
read_behave = LBehave()

jewelry_obj=read_behave.read_locators(Config.read_locators)
print(jewelry_obj)

class Jewelry:
    def __init__(self,driver):
        self.driver = driver

    def Jewelry_module(self):
        self.driver.find_element(*jewelry_obj["txt_jewelry"]).click()
        time.sleep(2)


    def sort_by(self):
        self.driver.find_element(*jewelry_obj['sort_by']).click()

        time.sleep(2)
        self.driver.find_element(*jewelry_obj['sort_by1']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['sort_by2']).click()
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['sort_by3']).click()
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['sort_by4']).click()
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['sort_by5']).click()
        time.sleep(3)

    def display(self):
        E3 = self.driver.find_element(*jewelry_obj['txt_display'])
        obj_ = Select(E3)
        obj_.select_by_index(0)
        time.sleep(3)
        self.driver.back()

    # def display2(self):
    #     E3 = self.driver.find_element(*jewelry_obj['txt_display'])
    #     obj_ = Select(E3)
    #     obj_.select_by_index(2)

    def View_As(self):
        time.sleep(2)
        E4 = self.driver.find_element(*jewelry_obj['txt_view'])
        obj_ = Select(E4)
        obj_.select_by_visible_text("List")
        time.sleep(3)
        self.driver.back()


    def Filter_By_Price(self):
        self.driver.find_element(*jewelry_obj['txt_filter1']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['txt_filterR1']).click()
        time.sleep(2)

        self.driver.find_element(*jewelry_obj['txt_filter2']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['txt_filterR2']).click()
        time.sleep(2)

        self.driver.find_element(*jewelry_obj['txt_filter3']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['txt_filterR3']).click()
        time.sleep(2)

    def ATC_dis(self):
        l_1 = ["Create Your Own Jewelry", "Black & White Diamond Heart", "Diamond Pave Earrings",
               "Diamond Tennis Bracelet", "Vintage Style Three Stone Diamond Engagement Ring"]
        for item in l_1:
            self.driver.find_element("xpath", f"//a[text() = '{item}']").click()
            time.sleep(2)
            self.driver.back()

    # def AddToCart(self):
    #     atc = self.driver.find_element(*jewelry_obj['addToCart'])
    #     return atc
    #
    # def Ratings(self):
    #     rate = self.driver.find_element(*jewelry_obj['rate'])
    #     return rate

    def Create_Your_Own_Jewelry(self):
        self.driver.find_element(*jewelry_obj["txt_Jewelry23"]).click()

    def J_Material(self):
        E6 = self.driver.find_element(*jewelry_obj['jMaterial'])
        time.sleep(3)
        obj_ = Select(E6)
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['Material1']).click()
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['Material2']).click()
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['Material3']).click()
        time.sleep(3)

    def length(self,length_):
        E7 = self.driver.find_element(*jewelry_obj['txt_length']).send_keys(length_)
        time.sleep(3)

    def pendant_radio(self):
        time.sleep(3)
        self.driver.find_element(*jewelry_obj['txt_radio1']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['txt_radio2']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['txt_radio3']).click()
        time.sleep(2)
        self.driver.find_element(*jewelry_obj['txt_radio4']).click()
        time.sleep(2)

