# https://piprogramming.org/articles/How-to-make-Selenium-undetectable-and-stealth--7-Ways-to-hide-your-Bot-Automation-from-Detection-0000000017.html
from gazpacho import Soup

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.keys import Keys

# https://pypi.org/project/webdriver-manager/
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import time

base_url = 'https://www.google.com/finance'
label_class = 'gyFHrc'
value_class = 'P6K39c'
input_box_class = 'Ax4B8'

ticker = 'TSLA'

chrome_options = ChromeOptions()
# chrome_options.AddUserProfilePreference("profile.default_content_setting_values.cookies", 2)
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--disable-extensions")

driver = Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
                options=chrome_options)
driver.get(base_url)
wait = WebDriverWait(driver, 15)

# wait for the input box
wait.until(EC.presence_of_element_located((By.CLASS_NAME, input_box_class)))
# get the input class, enter the ticker and press enter
input_widget = driver.find_elements(By.CLASS_NAME, input_box_class)
input_box = input_widget[1]
input_box.send_keys(ticker + Keys.ENTER) # theoretically, this should send request but does not
input_box.send_keys(Keys.RETURN) # so sending it again

# check the output on the right side is there
wait.until(EC.presence_of_element_located((By.CLASS_NAME, label_class)))
stuff = driver.find_elements(By.CLASS_NAME, label_class)
# print(f"stuff-->{stuff}")
for elem in stuff:
    html = elem.get_attribute("outerHTML")
    # print(f'html:{html}')
    soup = Soup(html)
    label = soup.find('div', {'class': label_class})
    value = soup.find('div', {'class': value_class})
    print(f'{label.text}: {value.text}')

driver.close()
