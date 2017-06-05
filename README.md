Зависимости:
    1. selenium
    2. chrome headless
    3. chrome webdriver
    4. elasticsearch
    5. docker

ТЗ:
1. selenium + headlessChrome: получаль страницы сайтов, навигация по ним.
2. elasticsearch для хранения данных и поиска по ним.
3. docker для маштабирования

Задания:
1. Нужно собрать пример:

 Заходим на яндекс ищем строку "суд" и первые 5 сайтов с глубиной в одну ссылку записываем в elasticsearch.
 elasticsearch пробуем найти адрес
 Все это должно запускаться в docker-контейнере.

https://github.com/elastic/elasticsearch-dsl-py
https://docs.scrapy.org/en/latest/intro/tutorial.html#intro-tutorial

https://duo.com/blog/driving-headless-chrome-with-python
https://github.com/ragingwind/chrome-headless-launcher
https://pythondigest.ru/view/11320/
https://github.com/segment-srl/htcap

http://wiki.python.su/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8/BeautifulSoup


lxml, beatifulsoup используются для навигации по html, нам это не нужно. chrome из коробки дает всю работу с DOM.
scrapy интересный фреймворк. нужно его посмотреть, думаю там много чего полезного будет.
Например, интересная логика работы с пауками:
1. их можно параллелить
2. каждый будет выполнять свои действия

вообще частью получения данных из веба и поиском на странице будет заниматься selenium+chrome.
Впринципе scrapy можно взять за основу логики парсинга.

elasticsearch понадобится для морфологического разбора и полнотекстового поиска среди всех данных.
Т.е если selenium+chrome будет отвечать за навигацию и получение данных, то elasticsearch за
первичную обработку и поиск в загруженных данных.

