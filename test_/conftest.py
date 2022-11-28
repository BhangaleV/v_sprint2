import pytest
from selenium import webdriver
from Library.config import Config
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# firefox_path = webdriver.Firefox(GeckoDriverManager().install())
@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver=webdriver.Chrome(ChromeDriverManager().install())

    elif request.param == "Firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())

    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    print(driver.title)
    driver.save_screenshot("Jewelry_screenshot.png")
    driver.close()
