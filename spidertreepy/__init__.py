__version__ = "0.0.1"

import os
import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = 'C:\\Users\\vgorbachev\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'

driver = webdriver.Chrome(
    executable_path=os.path.abspath("../driver/chromedriver.exe"),
    chrome_options=chrome_options
)
print("..start get")
driver.get("http://ya.ru")

print("..start fill")
search = driver.find_element_by_css_selector("input.input__control.input__input")
if search.is_displayed():
    search.send_keys('Я люблю Юлю')

print("..search")
menu_button = driver.find_element_by_css_selector("button.button_theme_websearch")
if menu_button.is_displayed():
    menu_button.click()

# driver.find_element_by_css_selector("documant")
# element.get_attribute('innerHTML')
print(driver.page_source)
w = codecs.open("test.html", "w", "utf-8")
w.write(driver.page_source)
w.close()
print("..end")
# assert "Looking Back at Android Security in 2016" in driver.page_source   driver.close()
