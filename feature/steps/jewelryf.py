import time
from behave import *
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

@given(u'Open the browser and enter demo web shop url and click on jewelry category')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    context.driver.maximize_window()
    context.driver.find_element("xpath", "//a[@href='/jewelry']").click()


@then(u'Click on sort by dropdown list options')
def step_impl(context):
    context.driver.find_element("id","products-orderby").click()



@then(u'Click on "Name: A to Z" then "Name: Z to A" then "Price: Low to High" then "Price: High to Low" then "Created On"')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element("xpath","//option[@value='https://demowebshop.tricentis.com/jewelry?orderby=5']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//option[@value='https://demowebshop.tricentis.com/jewelry?orderby=6']").click()
    time.sleep(3)
    context.driver.find_element("xpath","//option[@value='https://demowebshop.tricentis.com/jewelry?orderby=10']").click()
    time.sleep(3)
    context.driver.find_element("xpath","//option[@value='https://demowebshop.tricentis.com/jewelry?orderby=11']").click()
    time.sleep(3)
    context.driver.find_element("xpath","//option[@value='https://demowebshop.tricentis.com/jewelry?orderby=15']").click()
    time.sleep(3)

@then(u'Click on Display by')
def step_impl(context):
    context.driver.find_element("xpath","//select[@id='products-pagesize']").click()


@then(u'Click on 4 then 8 then 12')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element("xpath","//select[@id='products-pagesize']//option[text()='4']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//select[@id='products-pagesize']//option[text()='8']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//select[@id='products-pagesize']//option[text()='12']").click()

@then(u'Click on Filter By Price')
def step_impl(context):
    context.driver.find_element("xpath","//div[@class='filter-title']").click()



@then(u'Click on filter by 0.00-500.00 then 500.00-700.00 then 700.00-2000.00')
def step_impl(context):
    context.driver.find_element("xpath", '//span[text()="0.00"]/..//span[text()="500.00"]').click()
    time.sleep(2)
    context.driver.back()
    # context.driver.find_element("xpath", "//a[@href='https://demowebshop.tricentis.com/jewelry']").click()
    time.sleep(2)

    context.driver.find_element("xpath", '//span[text()="500.00"]/..//span[text()="700.00"]').click()
    time.sleep(2)
    context.driver.back()
    # context.driver.find_element("xpath", "//a[@href='https://demowebshop.tricentis.com/jewelry']").click()
    time.sleep(2)

    context.driver.find_element("xpath", '//span[text()="700.00"]/..//span[text()="3000.00"]').click()
    time.sleep(2)
    context.driver.back()
    # context.driver.find_element("xpath", "//a[@href='https://demowebshop.tricentis.com/jewelry']").click()
    time.sleep(2)


@then(u'Click on View as')
def step_impl(context):
    context.driver.find_element("xpath", '//select[@id="products-viewmode"]').click()


@then(u'Click on Grid As View and then List As View')
def step_impl(context):
    context.driver.find_element("xpath", "//select[@id='products-viewmode']//option[text()='List']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-viewmode']//option[text()='Grid']").click()
    time.sleep(6)


@then(u'Click on one of the product and check the description')
def step_impl(context):
    context.driver.find_element("xpath","//a[text()='Create Your Own Jewelry']").click()
    time.sleep(2)
    context.driver.back()


@then(u'come back and click on another product description and come back')
def step_impl(context):
    context.driver.find_element("xpath",'//a[text()="Vintage Style Three Stone Diamond Engagement Ring"]').click()
    time.sleep(2)
    context.driver.back()

@then(u'click on another product description')
def step_impl(context):
    context.driver.find_element("xpath",'//a[text()="Diamond Tennis Bracelet"]').click()
    time.sleep(2)
    context.driver.back()

@then(u'come back and click on another product description')
def step_impl(context):
    context.driver.find_element("xpath","//a[text()='Diamond Pave Earrings']").click()
    time.sleep(2)
    context.driver.back()

@then(u'come back and click on another product')
def step_impl(context):
    context.driver.find_element("xpath","//a[text()='Black & White Diamond Heart']").click()
    time.sleep(2)
    context.driver.back()

@then(u'click on Create Your Own Jewelry')
def step_impl(context):
    context.driver.find_element("xpath","//a[text()='Create Your Own Jewelry']").click()

@then(u'Click on Material dropdown list Options')
def step_impl(context):
    context.driver.find_element("xpath","//select[@id='product_attribute_71_9_15']").click()
    time.sleep(2)

@then(u'Click on "Gold 0,5mm" then "Gold 1mm" then "Silver 1mm"')
def step_impl(context):
    context.driver.find_element("xpath","//option[@value='45']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//option[@value='46']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//option[@value='47']").click()
    time.sleep(2)

@then(u'Enter the length in Length in cm Field')
def step_impl(context):
    context.driver.find_element("xpath","//input[@class='textbox']").send_keys("10")

@then(u'CLick on Pendant Radio Button Option')
def step_impl(context):
    context.driver.find_element("id","product_attribute_71_11_17_48").click()
    time.sleep(2)

@then(u'Click on "Ladybug" then "Heart" then "Star" then "None"')
def step_impl(context):
    context.driver.find_element("id","product_attribute_71_11_17_49").click()
    time.sleep(2)
    context.driver.find_element("id","product_attribute_71_11_17_50").click()
    time.sleep(2)
    context.driver.find_element("id","product_attribute_71_11_17_51").click()
    time.sleep(2)

@then(u'close the browser')
def step_impl(context):
    context.driver.close()
