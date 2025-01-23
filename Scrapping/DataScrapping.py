from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

asset = "PALANTIR"

driver = webdriver.Firefox()
driver.get("https://finance.yahoo.com")

try:
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                               '//button[@id="scroll-down-btn"]'))).click()

    driver.find_element(By.XPATH, '//button[@class="btn secondary accept-all "]').click()

    search_bar = driver.find_element(By.XPATH, '//input[@id="ybar-sbq"]')
    search_bar.click()
    search_bar.send_keys(asset + Keys.ENTER)

    historical_data_button = WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH, '//span[text()="Historical Data"]')))

    historical_data_button.click()

    dates_button = WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH, '//span[@class="label yf-1th5n0r"]')))

    dates_button.click()

    driver.find_element(By.XPATH, '//button[@value="5_Y"]').click()


finally:
    WebDriverWait(driver, 10)
