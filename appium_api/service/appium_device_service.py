from appium import webdriver
from appium_api.domain.desired_capabilities import DesiredCapabilities

# local appium 서버
appium_server = 'http://127.0.0.1:4723/wd/hub'


# 요청 값을 통해 driver 를 추출
def get_driver(desired_capabilities: DesiredCapabilities):
    return webdriver.Remote(appium_server, desired_capabilities.to_map())
