from selene import browser
from selene import be, have
import pytest

@pytest.fixture()
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def browser_open(browser_size):
    browser.open('https://google.com')

def test_search_pozitive(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_negative(browser_open):
    browser.element('[name="q"]').should(be.blank).type('***&*^%^&*^&31gflk134gkrv134gr').press_enter()
    browser.element('.card-section').should(have.text('По запросу ***&*^%^&*^&31gflk134gkrv134gr ничего не найдено'))



