from selenium import webdriver
from selenium.webdriver.chrome.options import Options
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
driver.get("https://portal.azure.com")

username = "ba"
 
# find the id or name or class of
# username by inspecting on username input
driver.find_element_by_name("loginfmt").send_keys(username)
   
