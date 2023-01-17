DRIVER_PATH_CHROME = 'driver/chromedriver.exe'
URL = 'https://b2c.passport.rt.ru'
ACTIVE_TAB = 'rt-tab--active'
TAB_BUTTONS = ['t-btn-tab-phone', 't-btn-tab-mail', 't-btn-tab-login', 't-btn-tab-ls']
PLACE_HOLDER_INPUT = ['Мобильный телефон', 'Электронная почта', 'Логин', 'Лицевой счёт']
TAB_TITLES = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
SEND_KEYS = ['79236955560', 'Dyundikov97@mail.ru', 'AbuBandit', '887766554433']
SEND_KEY_CAPTCHA = 'SkillFk'
REG_FIRST_NAME = ['И', 'Ив']
REG_LAST_NAME = ['Д', 'дю']
REG_ADRRES = ['И', '+79999999999', 'Dyundikov97@mail.ru']
REG_PASS = ['q', 'qwertyui', 'effaclar', 'effaclar9', 'Effaclar33']
REG_PASS_CONFIRM = ['Effaclar22', 'Effaclar33']


REG_KEYS_DICT = {
    'firstName': REG_FIRST_NAME,
    'lastName': REG_LAST_NAME,
    'address': REG_ADRRES,
    'password': REG_PASS,
    'password-confirm': REG_PASS_CONFIRM
}


REG_ERROR_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
REG_ERROR_ADDRES = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
REG_ERRORS_PASS = [
    'Длина пароля должна быть не менее 8 символов',
    'Пароль должен содержать только латинские буквы',
    'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру',
    'Пароль должен содержать хотя бы одну заглавную букву'
]
REG_ERROR_PASS_CONFIRM = 'Пароли не совпадают'

LOG_GOOGLE = 'Google Аккаунты'
LOG_YA = 'Авторизация'
LOG_VK = 'VK | Login'
LOG_OK = 'OK'
LOG_MAIL = 'Mail.Ru — Access request'
