from selenium.webdriver.common.by import By
from utils.navegador import crear_navegador
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_inventario():
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
        
        logging.info("Inventario verificado: %s productos encontrados", len(productos))


    except Exception:
        driver.save_screenshot("capturas/error_inventario.png")
        raise

    finally:
        driver.quit()