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

base_url = 'https://www.micasa.ch/de'
label_class = '_2iSKG9Ld4FFS-NR07Yox4M'
value_class = '_1JnScY_G48CqZrTq6G2aK-'
link_class = 'u-reset'
input_box_class = 'form-field--input'
load_more_xpath = "//*[@id='load-more-button']"
search_term = 'tischlampen'


def extract_elements(stuff):
    # print(f"stuff-->{stuff}")
    print(f'type: {type(stuff)}, len: {len(stuff)}')
    for elem in stuff:
        html = elem.get_attribute("outerHTML")
        # print(f'html:{html}')
        soup = Soup(html)
        link = soup.find('a', {'class': link_class}).attrs['href']
        label = soup.find('div', {'class': label_class})
        value = soup.find('div', {'class': value_class})
        print(f'{label.text}:{value.text}:{link}')


chrome_options = ChromeOptions()
driver = Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
                 options=chrome_options)

driver.get(base_url)

wait = WebDriverWait(driver, 15)

# wait for the input box
wait.until(EC.presence_of_element_located((By.CLASS_NAME, input_box_class)))
# get the input class, enter the ticker and press enter
input_widget = driver.find_elements(By.CLASS_NAME, input_box_class)
input_box = input_widget[0]
input_box.send_keys(search_term + Keys.ENTER)

# wait for load more button and click once
driver.execute_script("arguments[0].click();",
                      wait.until(EC.element_to_be_clickable((By.XPATH, load_more_xpath))))

# wait.until(EC.presence_of_element_located((By.ID, load_mode_id)))
# load_button = driver.find_elements(By.ID, load_mode_id)
# load_button[0].click()

# wait for load more button and this time extract
wait.until(EC.presence_of_element_located((By.XPATH, load_more_xpath)))
stuff = driver.find_elements(By.CLASS_NAME, '_2T3b0we9br-3owTUrx1Zx8')
extract_elements(stuff)
driver.close()

# local testing single loads
# driver.get('file:////Users/anirudh/Documents/Python/GitHub/scraping-learn/tischlampen.html')
# # stuff = driver.find_elements(By.CLASS_NAME, '_2T3b0we9br-3owTUrx1Zx8')
# # extract_elements(stuff)
# load_button = driver.find_elements(By.ID, load_mode_id)
# # print(f'load_button: {load_button}')
# print(f'type: {type(load_button)}, len: {len(load_button)}')
# driver.close()
