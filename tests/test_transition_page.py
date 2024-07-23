from pages.transitions_page import TransitionPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
import data
import allure
import pytest

@allure.suite('Тесты переходов по ссылкам в хэдере')
class TestTransitionPage:

    @allure.title('Переход на страницу "Самоката" по логотипу "Самоката"')
    @allure.description('Кликаем на кнопку «Заказать» вверху страницы, переходим к форме заказа, '
                        'кликаем на логотип "Самоката" и проверяем переход на главную страницу')
    def test_transition_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.go_to_order_page()

        order_page = OrderPage(driver)
        header = order_page.get_person_info_header()
        assert header.text == data.PERSON_INFO_HEADER

        page = TransitionPage(driver)
        page.go_to_main_page_by_scooter_logo()

        main_page_header_text = main_page.get_main_header_text()
        assert data.HEADER_SCOOTER in main_page_header_text

    @allure.title('Переход на страницу Дзен при нажатии на логотип "Яндекс"')
    @allure.description('Кликаем на логотип «Яндекс» в хэдере, переходим на страницу Дзен и проверяем, '
                        'что мы находимся на странице Дзен, найдя заголовок "Новости"')
    def test_transition_by_yandex_logo(self, driver):
        page = TransitionPage(driver)
        page.accept_cookies()
        page.go_to_dzen_by_yandex_logo()

        dzen_news_title = page.get_dzen_news_title()
        assert dzen_news_title == data.DZEN_NEWS_TITLE
