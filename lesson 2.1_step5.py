from selenium import webdriver

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
# open browser
# count x

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
# set formula
fol = browser.find_element_by_id('answer')
fol.send_keys(y)
# set radio
option1 = browser.find_element_by_css_selector("[for='robotsRule']")
option1.click()

browser.find_element_by_css_selector("[for='robotCheckbox']").click()
# sent form
button = browser.find_element_by_css_selector("button.btn")
button.click()
