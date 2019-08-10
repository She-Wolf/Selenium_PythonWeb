import time
import math
from selenium import webdriver

browser = webdriver.Chrome()


def main():
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    buttonClick()
    confirmAccept()
    # На новой странице решить капчу для роботов, чтобы получить число c ответом
    value = browser.find_element_by_id("input_value").text
    fillByID("answer", ln(value))
    buttonClick()
    time.sleep(5)
    browser.quit()


def fillByID(name, text):
    return browser.find_element_by_id(name).send_keys(text)


def buttonClick():
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def confirmAccept():
    confirm = browser.switch_to.alert
    confirm.accept()


def ln(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    main()
