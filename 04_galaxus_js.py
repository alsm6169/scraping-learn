from gazpacho import get, Soup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

base_url = 'https://galaxus.ch/'
suffix = '/en/liveshopping/82'

options = Options()
options.headless = True
service = Service('/usr/local/bin/geckodriver')
browser = Firefox(service=service, options=options)


browser.get(base_url+suffix)
wait = WebDriverWait(browser, 5)

class_name = 'sc-qlvix8-0'
wait.until(presence_of_element_located((By.CLASS_NAME, class_name)))
stuff = browser.find_elements(By.CLASS_NAME, class_name)
# print(f'stuff-->{stuff}')
for elem in stuff:
    html = elem.get_attribute("outerHTML")
    # print(f'html:{html}')
    soup = Soup(html)
    elem = soup.find('a')

    print(f'label: {elem.attrs["aria-label"]}, href: {base_url+elem.attrs["href"]}')

browser.close()