from selene.support.shared import browser
from selene import be, have


def test_search_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_empty_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('kjefhjhfjsdhfjsdfjdsgfjhsgdjfgsjhfgjhgfj').press_enter()
    browser.element('.card-section').should(have.text('ничего не найдено'))


