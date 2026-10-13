from selenium.webdriver.common.by import By
from utils.navegador import crear_navegador
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_carrito():
    driver = crear_navegador()

    try:
        driver.get("https://www.saucedemo.com")

        usuario = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.ID, "user-name"))
        )
        usuario.send_keys("standard_user")

        contrasena = driver.find_element(By.ID, "password")
        contrasena.send_keys("secret_sauce")

        driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        assert "/inventory.html" in driver.current_url

        titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
        assert titulo == "Products"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

        nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        productos[0].find_element(By.TAG_NAME, "button").click()

        contador = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text
        assert contador == "1"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        producto_carrito = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        ).text
        assert producto_carrito == nombre
        
        logging.info("Carrito verificado: producto %s agregado correctamente", nombre)


    except Exception:
        driver.save_screenshot("capturas/error_carrito.png")
        raise

    finally:
        driver.quit()