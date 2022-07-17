from appium.webdriver.webdriver import WebDriver
from src.sql_alchemy.db_model.account import Account
from src.sql_alchemy.db_model.macro import DriverType
from src.sub_process.domain.adb.device_info import DeviceInfo


# appium 구동에 필요한 디바이스 정보
class Device:
    device_info: DeviceInfo
    app_driver: WebDriver | None
    web_driver: WebDriver | None

    account: Account

    def __init__(self, device_info: DeviceInfo, app_driver: WebDriver | None, web_driver: WebDriver | None):
        self.device_info = device_info
        self.app_driver = app_driver
        self.web_driver = web_driver

    def get_driver_of_type(self, driver_type: DriverType):
        if driver_type is DriverType.APP: return self.app_driver
        if driver_type is DriverType.WEB: return self.web_driver
        else: return None
