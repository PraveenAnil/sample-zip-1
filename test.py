from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
driver.get("replacel")

username = "replaceus"
password = "replacepa"
# find the id or name or class of
# username by inspecting on username input
driver.find_element_by_name("loginfmt").send_keys(username)
driver.find_element_by_id("idSIButton9").click()

delay = 10 # seconds
myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'i0118')))

driver.find_element_by_name("passwd").send_keys(password)
WebDriverWait(driver, delay)
driver.find_element_by_id("idSIButton9").click()

   
