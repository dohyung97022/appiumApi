# sb 에 사용되는 xPath 모음
class SbXpath:
    BASE_MENU = "//li[@class='menu']"
    LOGIN_BUTTON = "//a[@class='users_login_link']"
    LOGIN_USERNAME_INPUT = "//input[@id='log_username']"
    LOGIN_PASSWORD_INPUT = "//input[@id='log_password']"
    LOGIN_SUBMIT = "//button[@type='submit']"
    UPLOAD_BUTTON = "//a[@class='upload ']"
    UPLOAD_BROWSE_BUTTON = "//span[@class='upload_button']"

    REGISTER_BUTTON = "//a[@class='users_register_link']"
    REGISTER_USERNAME_INPUT = "//input[@id='reg_username']"
    REGISTER_PASSWORD_INPUT = "//input[@id='reg_password']"
    REGISTER_EMAIL_INPUT = "//input[@id='reg_email']"
    REGISTER_REMODAL = "//div[@class='auth-remodal']"
    REGISTER_SUBMIT = "//button[@type='submit']"

    RECAPCHA_CHECKBOX = "//div[@class='recaptcha-checkbox-checkmark']"
