# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# def crear_navegador():
#     options = Options()
#     options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

#     driver = webdriver.Chrome(options=options)
#     return driver


from selenium import webdriver


def crear_navegador():
    driver = webdriver.Chrome()
    return driver