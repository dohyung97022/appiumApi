from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from src.sb.domain.common.sb_xpath import SbXpath
from src.dot_env.domain.sb import Sb
import time

from src.automation.domain.user import User


def goto_sb(driver: WebDriver):
    driver.get(Sb.website)


def register_sb(driver: WebDriver, user: User):
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.BASE_MENU).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_BUTTON).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_USERNAME_INPUT).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_USERNAME_INPUT).send_keys(user.username)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_PASSWORD_INPUT).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_PASSWORD_INPUT).send_keys(user.user_pw)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_EMAIL_INPUT).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_EMAIL_INPUT).send_keys(user.user_email)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.REGISTER_SUBMIT).click()


def login_sb(driver: WebDriver, user: User):
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.BASE_MENU).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.LOGIN_BUTTON).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.LOGIN_USERNAME_INPUT).click()
    driver.find_element(AppiumBy.XPATH, SbXpath.LOGIN_USERNAME_INPUT).send_keys(user.user_email)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.LOGIN_PASSWORD_INPUT).click()
    driver.find_element(AppiumBy.XPATH, SbXpath.LOGIN_PASSWORD_INPUT).send_keys(user.user_pw)
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.LOGIN_SUBMIT).click()


def upload_video(driver: WebDriver):
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.BASE_MENU).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.UPLOAD_BUTTON).click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, SbXpath.RECAPCHA_CHECKBOX).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, SbXpath.UPLOAD_BROWSE_BUTTON).click()
    time.sleep(3)
    ## 해당 동영상을 업로드한다.

    ## 해당 동영상을 삭제한다.
    ## s3 에서 해당 동영상의 metadata 안에 이미 사용되었다고 표기한다.
