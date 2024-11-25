from selene import browser
import pytest


@pytest.fixture(scope="session", autouse=True)
def browser_start():
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()