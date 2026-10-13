# Pre-Entrega – Automation Testing

## Descripción del proyecto

Este proyecto forma parte de la Pre-Entrega del curso de Automation Testing.

El objetivo es automatizar pruebas funcionales de la página [SauceDemo](https://www.saucedemo.com/) utilizando Python, Selenium y Pytest.

## Pruebas automatizadas

El proyecto incluye tres pruebas:

- **Login:** verifica que un usuario válido pueda iniciar sesión correctamente.
- **Inventario:** comprueba que se muestre el título "Products" y que existan productos disponibles.
- **Carrito:** agrega un producto al carrito y verifica que el contador y el producto sean correctos.

## Tecnologías utilizadas

- Python 3.11
- Selenium WebDriver
- Pytest
- pytest-html
- Brave Browser
- Git y GitHub
- Visual Studio Code

## Instalación

Para instalar las dependencias necesarias, ejecutar el siguiente comando en la terminal:

```powershell
python -m pip install selenium pytest pytest-html
```

## Ejecución de las pruebas

Para ejecutar los tres tests automatizados, abrir una terminal en la carpeta principal del proyecto y ejecutar:

```powershell
python -m pytest tests/ -v
```

Para ejecutar las pruebas y generar un reporte HTML:

```powershell
python -m pytest tests/ -v --html=reporte.html --self-contained-html
```

El reporte se guarda en el archivo `reporte.html` y puede abrirse con un navegador.