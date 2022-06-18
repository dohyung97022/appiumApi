from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from src.chrome_driver.domain.common.chrome_resource_id import ChromeResourceId
from src.chrome_driver.domain.common.chrome_resource_xpath import ChromeResourceXpath
import os
import re
import time


# 앞자리 버전에 맞는 드라이버의 위치를 반환
def get_driver_location_of_base_version(base_version: str):
    location = os.getcwd() + '/src/chrome_driver/drivers/'
    versions = os.listdir(location)
    version = find_base_version_from_list(base_version, versions)
    if version is None:
        # TODO : 해당 버전이 없을 경우 다운로드 받는 기능 구현
        raise LookupError('해당 chromedriver 버전을 찾을 수 없습니다. base_version = ' + base_version)
    return location + version


# 버전의 list 들 중 base 가 일치할 경우 반환
def find_base_version_from_list(base_version: str, versions: list[str]):
    for version in versions:
        if base_version == get_base_app_version(version):
            return version
    return None


# 앱 버전에서 base 버전 반환
def get_base_app_version(app_version: str):
    version = re.findall('([^\s]*)\.[^\s]*\.[^\s]*\.', app_version)
    if len(version) == 0:
        return None
    return version[0]


# 크롬을 통한 url 을 다운로드
def download_url(url: str, chrome_driver: WebDriver, app_driver: WebDriver):
    chrome_driver.get(url)
    time.sleep(3)
    app_driver.find_element(AppiumBy.ID, ChromeResourceId.OPTION_BUTTON).click()
    app_driver.find_element(AppiumBy.XPATH, ChromeResourceXpath.DOWNLOAD_BUTTON).click()
