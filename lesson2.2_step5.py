import math

from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    link = " http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # Считать значение для переменной x.
    value = int(browser.find_element_by_id("input_value").text)
    field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(str(ln(value)))
    # Выбрать чекбокс
    browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    # Выбрать радиобаттон
    browser.find_element_by_css_selector("[for='robotsRule']").click()
    # Нажать кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


# Посчитать математическую функцию от x.
def ln(x):
    math.log(abs(12 * math.sin(x)))


if __name__ == '__main__':
    main()
