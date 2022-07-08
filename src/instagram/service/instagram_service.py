from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from src.gmailnator.service.gmailnator_instagram_service import get_instagram_code_from_email
from src.instagram.domain.common.instagram_xpath import InstagramXpath
from src.sql_alchemy.db_model.account import Account
import time

instagram_site = 'https://www.instagram.com'


def goto_instagram(driver: WebDriver):
    time.sleep(3)
    driver.get(instagram_site)


def register_instagram(driver: WebDriver, user: Account):
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_BUTTON).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_BY_EMAIL).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_EMAIL_INPUT).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_EMAIL_INPUT).send_keys(user.user_email)
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NEXT).click()
    time.sleep(20)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_EMAIL_CODE_INPUT).click()

    # 이메일에서 코드 반환
    code = get_instagram_code_from_email(user.user_email)
    if code is None:
        return

    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_EMAIL_CODE_INPUT).send_keys(code)
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NEXT).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NAME_INPUT).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NAME_INPUT).send_keys(user.name)
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_PASSWORD_INPUT).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_PASSWORD_INPUT).send_keys(user.user_pw)
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NEXT).click()
    time.sleep(4)
    month_select = Select(driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_MONTH_SELECT))
    month_select.select_by_value(str(user.birthdate.month))
    time.sleep(4)
    date_select = Select(driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_DATE_SELECT))
    date_select.select_by_value(str(user.birthdate.day))
    time.sleep(4)
    year_select = Select(driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_YEAR_SELECT))
    year_select.select_by_value(str(user.birthdate.year))
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NEXT).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_AGREE_TERMS).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NEXT).click()
    time.sleep(4)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.REGISTER_NEXT).click()


def login_instagram(driver: WebDriver, user: Account):
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.LOGIN_BUTTON).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.LOGIN_USERNAME_INPUT).click()
    driver.find_element(AppiumBy.XPATH, InstagramXpath.LOGIN_USERNAME_INPUT).send_keys(user.user_id)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.LOGIN_PASSWORD_INPUT).click()
    driver.find_element(AppiumBy.XPATH, InstagramXpath.LOGIN_PASSWORD_INPUT).send_keys(user.user_pw)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.LOGIN_SUBMIT_BUTTON).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.SAVE_INFO_LATER).click()
    time.sleep(7)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.CANCEL).click()
    time.sleep(3)


def follow_others(driver: WebDriver):
    try:
        driver.find_element(AppiumBy.XPATH, InstagramXpath.LIKE).click()
    except:
        pass
    time.sleep(3)

    actions = ActionChains(driver)
    actions.scroll(1, 1, 1, 100, 5000)
    actions.perform()
    time.sleep(3)

    try:
        driver.find_element(AppiumBy.XPATH, InstagramXpath.LATER).click()
    except:
        pass
    time.sleep(3)

    driver.find_element(AppiumBy.XPATH, InstagramXpath.LIKE).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.FOLLOW).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.FOLLOW).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.FOLLOW).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.FOLLOW).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, InstagramXpath.FOLLOW).click()
