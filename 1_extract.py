import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv

load_dotenv()

DEFAULT_DIRECTORY = os.getenv('DEFAULT_DIRECTORY')


chrome_options = Options()
prefs = {"download.default_directory": r"{DEFAULT_DIRECTORY}"}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.list-org.com/search")
time.sleep(5)
work_checkbox = driver.find_element(by=By.ID, value="work")
time.sleep(5)
work_checkbox.click()
time.sleep(5)
email_checkbox = driver.find_element(by=By.ID, value="is_email")
time.sleep(5)
email_checkbox.click()
time.sleep(5)
okved_window = driver.find_element(by=By.ID, value="okved")
time.sleep(5)
okved_window.send_keys("49.1")
time.sleep(5)
sorted_curtain = Select(driver.find_element(by=By.ID, value="sort"))
time.sleep(3)
sorted_curtain.select_by_visible_text("прибыли ↑")
time.sleep(3)
button_search = driver.find_element(
    by=By.XPATH, value="//button[contains(text(),'Поиск')]"
)
time.sleep(3)
button_search.click()
time.sleep(15)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(8)
button_get_list = driver.find_element(
    by=By.XPATH, value="//a[@class='btn btn-outline-secondary m-1']"
)
time.sleep(3)
button_get_list.click()
time.sleep(15)
driver.quit()
