from appium.webdriver.webdriver import WebDriver
from src.sub_process.domain.adb.device_info import DeviceInfo


# appium 구동에 필요한 디바이스 정보
class Device:
    device_info: DeviceInfo
    app_driver: WebDriver
    web_driver: WebDriver

    def __init__(self, device_info: DeviceInfo, app_driver: WebDriver, web_driver: WebDriver):
        self.device_info = device_info
        self.app_driver = app_driver
        self.web_driver = web_driver
