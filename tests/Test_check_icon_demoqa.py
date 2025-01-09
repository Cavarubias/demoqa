from selenium.webdriver.common.by import By
from selenium import webdriver


def test_check_icon():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    # поиск элемента
    icon = driver.find_element(By.CSS_SELECTOR, '#app > header > a')
    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')