import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    # Запуск браузера перед каждым тестом
    options = Options()
    #options.add_argument("--headless")  # Запуск в безголовом режиме (без отображения окна браузера)
    driver_path = "C:\\ChromeDriver\\chromedriver.exe"
    service = Service(driver_path)
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    # Закрытие браузера после каждого теста
    browser.quit()

def test_example(browser):
    err = False

    # Открытие страницы
    browser.get("C:\\Users\\kosty\\Documents\\testovoe\\example.html")
    
    # Ввод текста в поле
    input_field = browser.find_element(By.XPATH, "//input[@id='my-input']")
    input_field.send_keys("Hello, World!")
    
    # Нажатие клавиши Enter
    input_field.send_keys(Keys.ENTER)
    
    # Проверка отображения элемента (изображения, текста и т.д.)
    image = browser.find_element(By.XPATH, "//img[@id='my-image']")
    assert image.is_displayed()
    
    # Проверка отображения мелкого элемента (красного поля ввода при ошибке)
    error_field = browser.find_element(By.XPATH, "//input[@class='error']")
    assert error_field.is_displayed()
    
    # Проверка появления нужного текста в элементе
    element = browser.find_element(By.XPATH, "//div[@id='my-element']")
    assert "Ожидаемый текст" in element.text

    # Клик по кнопке
    button = browser.find_element(By.XPATH, "//button[@id='my-button']")
    button.click()

    # Скриншот страницы
    browser.save_screenshot("screenshot1.png")

    # Переход по вкладкам
    browser.switch_to.window(browser.window_handles[1])
    # Далее можно выполнить проверку на открытие нужной вкладки

    # Скриншот страницы
    browser.save_screenshot("screenshot2.png")

    # ПРОВЕРКА СТРАНИЦЫ С ОШИБКАМИ
    if err:
        # Ввод текста в поле
        input_field = browser.find_element(By.XPATH, "//input[@id='my-input']")
        input_field.send_keys("Hello, World!")
        
        # Нажатие клавиши Enter
        input_field.send_keys(Keys.ENTER)
        
        # Проверка отображения элемента (изображения, текста и т.д.)
        image = browser.find_element(By.XPATH, "//img[@id='my-image']")
        assert image.is_displayed()
        
        # Проверка отображения мелкого элемента (красного поля ввода при ошибке)
        error_field = browser.find_element(By.XPATH, "//input[@class='error']")
        assert error_field.is_displayed()
        
        # Проверка появления нужного текста в элементе
        element = browser.find_element(By.XPATH, "//div[@id='my-element']")
        assert "Ожидаемый текст" in element.text

        # Клик по кнопке
        button = browser.find_element(By.XPATH, "//button[@id='my-button']")
        button.click()