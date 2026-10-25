import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    # browser = playwright_instance.chromium.launch(
    #     headless=False, slow_mo=1000
    # )  # чтобы видеть шаги
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def page(context):
    return context.new_page()
