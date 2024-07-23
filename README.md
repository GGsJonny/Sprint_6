# Sprint_6

Проект автоматизации тестирования сервиса «Яндекс.Самокат»

## Используемые технологии

- pytest
- Selenium Web Driver 3.x
- Allure Report
- Mozilla Firefox

## Структура проекта

Проект состоит из трёх папок и директории с отчетами Allure

### Папка `tests`

Содержит модули с автоматизированными тестовыми сценариями:

- `test_main_page.py` - содержит class `TestMainPage` с методами для тестирования главной страницы.
- `test_order_page.py` - содержит class `TestOrderPage` с методами для тестирования страницы заказа.
- `test_transition_page.py` - содержит class `TestTransitionPage` с методами для тестирования переходов по ссылкам в хэдере.

### Папка `pages`

Содержит page objects для тестируемых веб-страниц:

- `base_page.py` - class `BasePage` с общими методами.
- `main_page.py` - class `MainPage` с методами главной страницы.
- `order_page.py` - class `OrderPage` с методами страницы заказа.
- `transitions_page.py` - class `TransitionPage` с методами для тестирования переходов.

### Папка `locators`

Содержит модули с локаторами элементов для соответствующих страниц:

- `main_page_locators.py` - локаторы для главной страницы.
- `order_page_locators.py` - локаторы для страницы заказа.
- `transition_page_locators.py` - локаторы для страницы переходов.

### Директория `allure_results`

Содержит сгенерированные Allure-отчеты о результатах тестирования.
