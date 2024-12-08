import pytest
from playwright.sync_api import sync_playwright

BASE_URL='https://www.wikipedia.org'
API_URL='https://dummyjson.com' #  It uses https://jsonplaceholder.typicode.com/ for examle data

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
