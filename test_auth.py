from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import consts
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en-GB'})
    driver = webdriver.Chrome(executable_path=consts.DRIVER_PATH_CHROME, chrome_options=options)

    driver.get(consts.URL)
    driver.maximize_window()
    wait = WebDriverWait(driver, 40)

    assert wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="card-container__title"]'))).text == 'Авторизация'
    return driver, wait


def check_auth_failed(driver: webdriver, wait: WebDriverWait):
    driver.find_element(By.ID, ('kc-login')).click()

    driver.implicitly_wait(40)
    forgetLink = driver.find_element(By.LINK_TEXT, 'Забыл пароль')
    classesOfforgetLink = forgetLink.get_attribute('class')

    if check_captcha_visibility(driver, wait):
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.card-container__error')))
        assert title.text == 'Неверно введен текст с картинки'
    else:
        title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'p.card-container__error.login-form-container__error--bold')))
        assert title.text == 'Неверный логин или пароль'
        assert classesOfforgetLink.__contains__('rt-link--orange')

    time.sleep(3)
    driver.quit()


def check_captcha_visibility(driver: webdriver, wait: WebDriverWait):
    check = driver.find_element(By.CSS_SELECTOR, 'img.rt-captcha__image')
    if check is not None:
        return True
    else:
        return False


def test_form_change():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    tabButtons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rt-tab')))
    assert wait.until(EC.title_is('Ростелеком ID'))
    assert len(tabButtons) == 4

    for i in range(len(tabButtons)):
        actionChain.move_to_element(tabButtons[i]).click().perform()
        placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
        assert wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, consts.ACTIVE_TAB))).text == driver.find_element(By.ID,
                                                                                                           consts.TAB_BUTTONS[
                                                                                                               i]).text
        assert placeholderInput == consts.PLACE_HOLDER_INPUT[i], driver.quit()


def test_correct_change_input():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    tabButtons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rt-tab')))

    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == consts.PLACE_HOLDER_INPUT[0]

    for i in range(len(tabButtons)):
        actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
        actionChain.send_keys(consts.SEND_KEYS[i]).perform()

        actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()

        activeTabButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.ACTIVE_TAB}')))
        assert activeTabButton.text == consts.TAB_TITLES[i], driver.quit()

        time.sleep(1)  # Имитация живого пользователя

        actionChain.double_click(driver.find_element(By.ID, 'username')).click_and_hold().send_keys(
            Keys.DELETE).perform()
        time.sleep(1)

    driver.quit()


def test_correct_input_phone_number():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == consts.PLACE_HOLDER_INPUT[0]

    actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
    actionChain.send_keys('9236955560').perform()

    actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()
    actionChain.send_keys('qazwsxedc').perform()

    activeTabButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.ACTIVE_TAB}')))
    assert activeTabButton.text == consts.TAB_TITLES[0]

    check_auth_failed(driver, wait)


def test_correct_input_email():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == consts.PLACE_HOLDER_INPUT[0]

    actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
    actionChain.send_keys('Dyundikov97@mail.ru').perform()

    actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()
    actionChain.send_keys('qazwsxedc').perform()

    activeTabButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.ACTIVE_TAB}')))
    assert activeTabButton.text == consts.TAB_TITLES[1]

    check_auth_failed(driver, wait)


def test_correct_input_login():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == consts.PLACE_HOLDER_INPUT[0]

    actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
    actionChain.send_keys('abubandit').perform()

    actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()
    actionChain.send_keys('qazwsxedc').perform()

    activeTabButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.ACTIVE_TAB}')))
    assert activeTabButton.text == consts.TAB_TITLES[2]

    check_auth_failed(driver, wait)


def test_correct_input_ls():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)

    placeholderInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rt-input__placeholder'))).text
    assert placeholderInput == consts.PLACE_HOLDER_INPUT[0]

    actionChain.move_to_element(driver.find_element(By.ID, 'username')).click().perform()
    actionChain.send_keys('0123456789012').perform()

    actionChain.move_to_element(driver.find_element(By.ID, 'password')).click().perform()
    actionChain.send_keys('Qwertyui').perform()

    activeTabButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.ACTIVE_TAB}')))
    assert activeTabButton.text == consts.TAB_TITLES[3], driver.quit()
    check_auth_failed(driver, wait)


def test_auth_with_vk():
    driver, wait = get_driver()

    old_url = driver.current_url

    wait.until(EC.presence_of_element_located((By.ID, 'oidc_vk'))).click()

    wait.until(lambda driver_lambda: old_url != driver_lambda.current_url
                                     and driver.execute_script("return document.readyState == 'complete'"))

    assert wait.until(EC.title_is(consts.LOG_VK))
    assert driver.current_url.__contains__('https://oauth.vk.com')

    time.sleep(3)
    driver.quit()


def test_auth_with_ok():
    driver, wait = get_driver()

    old_url = driver.current_url

    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ok'))).click()

    wait.until(lambda driver_lambda: old_url != driver_lambda.current_url
                                     and driver.execute_script("return document.readyState == 'complete'"))

    assert wait.until(EC.title_is(consts.LOG_OK))
    assert driver.current_url.__contains__('https://connect.ok.ru')

    time.sleep(3)
    driver.quit()


def test_auth_with_mail():
    driver, wait = get_driver()

    old_url = driver.current_url

    wait.until(EC.presence_of_element_located((By.ID, 'oidc_mail'))).click()

    wait.until(lambda driver_lambda: old_url != driver_lambda.current_url
                                     and driver.execute_script("return document.readyState == 'complete'"))

    assert wait.until(EC.title_is(consts.LOG_MAIL))
    assert driver.current_url.__contains__('https://connect.mail.ru/oauth')

    time.sleep(3)
    driver.quit()


def test_auth_with_google():
    driver, wait = get_driver()

    old_url = driver.current_url

    wait.until(EC.presence_of_element_located((By.ID, 'oidc_google'))).click()

    wait.until(lambda driver_lambda: old_url != driver_lambda.current_url
                                     and driver.execute_script("return document.readyState == 'complete'"))

    assert wait.until(EC.title_contains(consts.LOG_GOOGLE))
    assert driver.current_url.__contains__('https://accounts.google.com/o/oauth2/auth')

    time.sleep(3)
    driver.quit()


def test_auth_with_ya():
    driver, wait = get_driver()

    old_url = driver.current_url

    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ya'))).click()

    wait.until(lambda driver_lambda: old_url != driver_lambda.current_url
                                     and driver.execute_script("return document.readyState == 'complete'"))

    assert wait.until(EC.title_contains(consts.LOG_YA))
    assert driver.current_url.__contains__('https://oauth.yandex.ru/') or driver.current_url.__contains__(
        'https://passport.yandex.ru/auth')

    time.sleep(3)
    driver.quit()


def test_correct_redirect_to_restore_password():
    driver, wait = get_driver()

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Забыл пароль'))).click()
    assert wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Восстановление пароля'

    driver.quit()


def test_correct_redirect_to_register():
    driver, wait = get_driver()

    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    driver.quit()