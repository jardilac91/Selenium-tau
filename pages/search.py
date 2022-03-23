"""
Este módulo contiene DuckDuckGoSearchPage,
la vista encargada de representar la página de búsqueda de DuckDuckGo
"""
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self,browser):
        self.browser = browser

    def load(self):
        # TODO
        pass

    def search(self, phrase):
        # TODO
        pass