from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd


def precioProducto(code):
    
    # Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver_path = './chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    # Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    time.sleep(1)

    # Inicializamos el navegador
    url = f"https://guatemaladigital.com/Producto/{code}"
    driver.get(url)

    price = driver.find_element( By.XPATH,  '//*[@id="columnaA"]/div[3]/h4[1]/span/span')
    price = price.text

    driver.quit()

    # "precioQuetzales":209,
    print("El precio es: ",price,"")

precioProducto(5041295)