import pytest as pytest
from selenium import webdriver
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def browsr():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=640,480')
    browser.config.driver_options = options
    yield browser
    browser.quit()


def test_search_selene(browsr):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_empty_result(browsr):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('kjefhjhfjsdhfjsdfjdsgfjhsgdjfgsjhfgjhgfj').press_enter()
    browser.element('.card-section').should(have.text('ничего не найдено'))


