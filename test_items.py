import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_find_basket_button_for_different_interface_languages(browser):
    try:
        browser.get(link)
        # ждем 30 секунд по условиям задания
        time.sleep(30)
        basket_button = WebDriverWait(browser, 10).until(
            # две строки для запуска рабочего варианта и падающего, раскомментируйте нужную.
            ## Рабочий вариант
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]"))
            ## падающий вариант
            #EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'knowingly_incorrect_selector')]"))
        )
    finally:
        # возвращаем assert если кнопка не найдена. Проверка реализована через наличие basket_button в переменных
        assert 'basket_button' in vars(), "WARNING: Basket button NOT found!"
