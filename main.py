import os

from appium.webdriver.common.appiumby import AppiumBy

from appium_api.service.appium_device_service import get_driver
from sub_process.service.subprocess_adb_service import get_all_adb_device_info


def example_appium():
    device_infos = get_all_adb_device_info()
    desired_capabilities = device_infos[0].to_desired_capabilities()
    driver = get_driver(desired_capabilities)
    driver.get('https://www.instagram.com')
    driver.find_element(AppiumBy.XPATH, "//button[text()='로그인']").click()


print(os.getcwd())