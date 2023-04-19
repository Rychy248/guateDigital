from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def precioProducto(code):
    
    url = f"https://guatemaladigital.com/Producto/{code}"
    driver = webdriver.Firefox()
    
    driver.get("http://www.python.org")
    
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

    # "precioQuetzales":209,
    print("El precio es: ",price,"")
    print(soup.get("h4"))

precioProducto(5041295)