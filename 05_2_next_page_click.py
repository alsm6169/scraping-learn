# https://piprogramming.org/articles/How-to-make-Selenium-undetectable-and-stealth--7-Ways-to-hide-your-Bot-Automation-from-Detection-0000000017.html
from gazpacho import Soup
from selenium.common import StaleElementReferenceException

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

base_url = 'https://www.lumimart.ch/de/'
label_class = 'product-item__name'
value_class = 'product-item__pricing__item'
value_class2 = 'product-item__price__value'
item_details_class = 'product-item__details'
# item_details_class = 'list-page__content product-list'
link_class = 'link--enclosing'
input_box_id = 'searchField-custom'
next_page = "//*[@id='site-wrapper']/main/div[2]/div[4]/div[2]/div[1]/a[4]"
next_page = "pagination__next"
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
        value = soup.find('dd', {'class': value_class2},partial=False)
        # value = soup.find('div', {'class': value_class})
        # print(f'type value: {type(value)}, value: {value}')
        # value = soup.find('div', {'class': value_class}).find('dd', {'class': value_class2})
        # print(f'type value: {type(value)}, value: {value}')
        #value = soup.find('div', {'class': value_class}).find('dd', {'class': value_class2})[0]
        # print(f'type value: {type(value)}, value: {value}')
        print(f'{label.text}:{value.text}:{link}')


chrome_options = ChromeOptions()
driver = Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
                 options=chrome_options)

driver.get(base_url)

wait = WebDriverWait(driver, 15)

# wait for the input box
wait.until(EC.presence_of_element_located((By.ID, input_box_id)))
# get the input class, enter the ticker and press enter
input_widget = driver.find_elements(By.ID, input_box_id)
print(f'input_widget> type: {type(input_widget)}, len: {len(input_widget)}')
input_box = input_widget[0]
input_box.send_keys(search_term + Keys.ENTER)

stuff = driver.find_elements(By.CLASS_NAME, item_details_class)
extract_elements(stuff)

print('clicking next')
# for i in range(4):
#     try:
driver.refresh()
# wait for load more button and click once
driver.execute_script("arguments[0].click();",
                      wait.until(EC.element_to_be_clickable((By.CLASS_NAME, next_page))))

# wait for load more button and this time extract
wait.until(EC.presence_of_element_located((By.CLASS_NAME, next_page)))
stuff = driver.find_elements(By.CLASS_NAME, item_details_class)
    # except StaleElementReferenceException as e:
    #     raise e
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
