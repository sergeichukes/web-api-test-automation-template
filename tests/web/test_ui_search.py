from playwright.sync_api import sync_playwright
from tests.conftest import BASE_URL


def test_sould_search_in_wikipedia():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск браузера (headless=False для визуализации)
        page = browser.new_page()

        # Шаг 1: Открыть главную страницу Википедии
        page.goto(BASE_URL)

        # Шаг 2: Ввести "Michael Jackson" в поле поиска
        search_input = page.locator("input[name='search']")
        search_input.fill("Michael Jackson")

        # Шаг 3: Нажать на кнопку поиска
        search_button = page.locator("button[type='submit']")
        search_button.click()

        # Шаг 4: Убедиться, что на странице результатов есть ссылка на статью о Майкле Джексоне
        page.wait_for_selector("text=Michael Jackson",)  # Ожидаем, что на странице будет текст "Michael Jackson"

        # Закрытие браузера
        browser.close()

