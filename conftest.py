import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", 
                    default="en", help="Write language for testing on prefered language")

@pytest.fixture(scope="function")
def browser(request):
    prefered_lang = request.config.getoption("language")
    if prefered_lang is None:
        raise pytest.UsageError("Please write option for '--language' when execute test")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': prefered_lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()