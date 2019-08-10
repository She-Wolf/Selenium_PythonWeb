from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "  http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x, y):
    return str(x + y)


# выбрать элементы по тексту, превратить в числа,
value1 = int(browser.find_element_by_id("num1").text)
value2 = int(browser.find_element_by_id("num2").text)
# найти выпадающий список, раскрыть его, выбрать элемент в соответствие со значением calc
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(calc(value1, value2))
button = browser.find_element_by_css_selector("button.btn")
button.click()
