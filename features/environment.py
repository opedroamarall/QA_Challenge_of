from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()