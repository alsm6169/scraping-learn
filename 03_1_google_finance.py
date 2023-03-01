# https://piprogramming.org/articles/How-to-make-Selenium-undetectable-and-stealth--7-Ways-to-hide-your-Bot-Automation-from-Detection-0000000017.html
# https://tilburgsciencehub.com/building-blocks/configure-your-computer/task-specific-configurations/configuring-python-for-webscraping/
# from bs4 import BeautifulSoup
from gazpacho import get, Soup

# pip install -U selenium
from selenium.webdriver import Firefox, Chrome, ChromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.core.utils import ChromeType
# https://pypi.org/project/webdriver-manager/
# pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


base_url = 'https://www.google.com/finance'
suffix = '/quote/ACN:NYSE'
html = get(base_url+suffix)
# class_name = 'gyFHrc'

# WORKING BEAUTIFUL SOUP
# soup = BeautifulSoup(html, 'html.parser')
# box_rows = soup.find_all("div", class_name)
# print(box_rows)
# for row in box_rows:
#     print(type(row), str(row.contents[1].contents))
# exit(1)
# box_rows = soup.find_all("div", "P6K39c")
# # print(box_rows)
# for row in box_rows:
#     print(type(row), str(row.contents))

label_class = 'gyFHrc'
value_class = 'P6K39c'

# WORKING GAZPACHO
# soup = Soup(html)
# rows = soup.find('div', {'class': label_class})
# for row in rows:
#     # print(type(row), row)
#     title = row.find('span')
#     value = row.find('div', {'class': value_class})
#     print(title.text, '=>', value.text)


# options = Options()
# options.headless = True
# browser = Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
# browser.get(base_url+suffix)
# wait = WebDriverWait(browser, 15)
#
# wait.until(presence_of_element_located((By.CLASS_NAME, label_class)))
# stuff = browser.find_elements(By.CLASS_NAME, label_class)
# print(f'stuff-->{stuff}')
# for elem in stuff:
#     html = elem.get_attribute("outerHTML")
#     # print(f'html:{html}')
#     soup = Soup(html)
#     elem = soup.find('div', {'class': label_class})
#
#     print(f'label: {elem.text}')
# browser.close()

## WORKING: as from help from stackoverflow
chrome_options = ChromeOptions()
# chrome_options.AddUserProfilePreference("profile.default_content_setting_values.cookies", 2)
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--disable-extensions")

# driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
                options=chrome_options)

label_class = 'gyFHrc'
value_class = 'P6K39c'
driver.get("https://www.google.com/finance/quote/ACN:NYSE")

wait = WebDriverWait(driver, 15)
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
