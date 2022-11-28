from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

# //open the link and maximize the window and click on jewelry module
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath","//a[@href='/jewelry']").click()

# element = driver.find_element("xpath", "//a[@href='/jewelry']")
# ac_obj = ActionChains(driver)
# ac_obj.move_to_element(element).perform()
# time.sleep(2)

#Click on Sort By Option
element1 = driver.find_element("xpath",'//select[@id="products-orderby"]')
obj1 = Select(element1)
obj1.select_by_visible_text("Position")
time.sleep(2)

obj1.select_by_visible_text("Name: A to Z")
time.sleep(2)
driver.back()

obj1.select_by_visible_text("Name: Z to A")
time.sleep(2)
driver.back()

obj1.select_by_visible_text("Price: High to Low")
time.sleep(2)
driver.back()

obj1.select_by_visible_text("Price: Low to High")
time.sleep(2)
driver.back()

obj1.select_by_visible_text("Created on")
time.sleep(2)
driver.back()

##Click on Sort By Display
element2 = driver.find_element("xpath",'//select[@id="products-pagesize"]')
obj2 = Select(element2)
obj2.select_by_visible_text("8")
time.sleep(2)

obj2.select_by_visible_text("4")
time.sleep(2)
driver.back()

obj2.select_by_visible_text("12")
time.sleep(2)
driver.back()

##Click on Sort By View As
element3 = driver.find_element("xpath",'//select[@id="products-viewmode"]')
obj3 = Select(element3)
obj3.select_by_visible_text("Grid")
time.sleep(2)


obj3.select_by_visible_text("List")
time.sleep(5)
driver.back()

##Click on Filter By Price
driver.find_element("xpath",'//span[text()="0.00"]/..//span[text()="500.00"]').click()
# obj4 = Select(element4)
# obj4.select_by_visible_text("0.00-500.00")
time.sleep(2)
driver.find_element("xpath","//a[@href='https://demowebshop.tricentis.com/jewelry']").click()
time.sleep(2)

driver.find_element("xpath",'//span[text()="500.00"]/..//span[text()="700.00"]').click()
time.sleep(2)
driver.find_element("xpath","//a[@href='https://demowebshop.tricentis.com/jewelry']").click()
time.sleep(2)

driver.find_element("xpath",'//span[text()="700.00"]/..//span[text()="3000.00"]').click()
time.sleep(2)
driver.find_element("xpath","//a[@href='https://demowebshop.tricentis.com/jewelry']").click()
time.sleep(2)

##to check add to cart is present or not
l_1=["Create Your Own Jewelry","Black & White Diamond Heart","Diamond Pave Earrings","Diamond Tennis Bracelet","Vintage Style Three Stone Diamond Engagement Ring"]
for item in l_1:
    driver.find_element("xpath",f"//a[text() = '{item}']").click()
    time.sleep(2)
    driver.back()

driver.find_element("xpath","(//h2[@class='product-title']/../..//input[@type='button'])[1]").click()
time.sleep(10)
driver.back()
driver.find_element("xpath","//a[@href='/black-white-diamond-heart']/../..//input[@value='Add to cart']").click()
time.sleep(2)



##Go in Create Your Own Jewelry
driver.find_element("xpath","(//a[@href='/create-it-yourself-jewelry'])[1]").click()  ##how to create obj and perform click action?

##Select material for Jewelry
element4 = driver.find_element("xpath",'//select[@id="product_attribute_71_9_15"]')
obj4 = Select(element4)
obj4.select_by_value("45")
time.sleep(2)

obj4.select_by_value("46")
time.sleep(2)

obj4.select_by_value("47")
time.sleep(2)

##Enter Length In Cm
driver.find_element("xpath",'//input[@class="textbox"]').send_keys("-10")
time.sleep(1)

##Pendant Radio Button
driver.find_element("xpath",'//input[@value="48"]').click()
time.sleep(2)
driver.find_element("xpath",'//input[@value="49"]').click()
time.sleep(2)
driver.find_element("xpath",'//input[@value="50"]').click()
time.sleep(2)
driver.find_element("xpath",'//input[@value="51"]').click()
time.sleep(2)







