from selenium.webdriver.common.by import By
from utils.navegador import crear_navegador
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_login_valido():
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

        logging.info("Login exitoso: usuario standard_user")

    
    except Exception:
        driver.save_screenshot("capturas/error_login.png")
        raise

    finally:
        driver.quit()