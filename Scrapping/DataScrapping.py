from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os

asset = "HBAR-USD"

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

    driver.find_element(By.XPATH, '//button[@value="MAX"]').click()

    tabla = driver.find_element(By.XPATH, '//tbody')
    filas = tabla.find_elements(By.TAG_NAME, 'tr')

    columnasNom = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]

    data = []
    for fila in filas:
        columnas = fila.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in columnas])

    df = pd.DataFrame(data, columns=columnasNom)

    ruta_carpeta_data = "../Data"

    df.to_excel(os.path.join(ruta_carpeta_data, "asset.xlsx"), index=False)

    print("Dataframe of data related to the asset in the last 5 years stored!")


finally:
    WebDriverWait(driver, 10)
