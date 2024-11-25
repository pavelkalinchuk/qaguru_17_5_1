from selene import browser
import pytest
from selenium import webdriver

# Ниже блок из трёх строк для решения проблемы с долгой загрузкой страницы
driver_options = webdriver.ChromeOptions()
driver_options.page_load_strategy = 'eager'
browser.config.driver_options = driver_options


@pytest.fixture(scope="session", autouse=True)
def browser_start():
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()