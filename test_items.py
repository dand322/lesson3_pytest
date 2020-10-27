import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_add_button_exist(browser):
    try:
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        time.sleep(10)
        return True
    finally:
        return False
    assert test_guest_add_button_exist(browser) == True, "Кнопка не найдена"

