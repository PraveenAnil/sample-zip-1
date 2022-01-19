from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
FIREFOXDRIVER_PATH = '/usr/local/bin/geckodriver'

firefoxOptions = Options()
firefoxOptions.add_argument('--start-maximized')
driver = webdriver.Firefox(executable_path=FIREFOXDRIVER_PATH, options=firefoxOptions )
driver.get("replacel")
driver.maximize_window()
username = "replaceus"
password = "replacepa"
# find the id or name or class of
# username by inspecting on username input
driver.find_element_by_name("username").send_keys(username)

time.sleep(2)
driver.find_element_by_name("password").send_keys(password)

time.sleep(2)
driver.find_element_by_id("signin_button").click()

driver.find_element_by_id("signin_button").send_keys(Keys.ENTER);
