import time

from selenium import webdriver
import os

browser = webdriver.Chrome()


def main():
    link = " http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # Заполнить поля
    fillByID("firstname", "Elena")
    fillByID("lastname", "God")
    fillByID("email", "email@email.com")
    # Прикрепить файл
    fillByID("file", sendFile("file.txt"))
   #Отправь, закрой
    buttonClick()




def fillByID(name, text):
    return browser.find_element_by_name(name).send_keys(text)


def sendFile(file):
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, file)  # добавляем к этому пути имя файла
    return file_path


def buttonClick():
    button = button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    browser.quit()


if __name__ == '__main__':
    main()
