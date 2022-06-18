from appium.webdriver.webdriver import WebDriver

from src.appium_api.domain.device import Device
from src.sub_process.domain.adb.device_info import DeviceInfo


# 현제 연결된 디바이스 정보
class CurrentDevices:
    udid_to_devices: dict[str, Device] = {}

    def __init__(self, device_infos: list[DeviceInfo], app_drivers: list[WebDriver], web_drivers: list[WebDriver]):
        for i in range(len(device_infos)):
            # app / web driver udid 일치 확인
            self.validate_driver_udid(app_drivers[i], device_infos[i])
            self.validate_driver_udid(web_drivers[i], device_infos[i])
            # 디바이스 정보
            device = Device(device_infos[i], app_drivers[i], web_drivers[i])
            # dict 저장
            self.udid_to_devices[device_infos[i].udid] = device

    @staticmethod
    def validate_driver_udid(driver: WebDriver, device_info: DeviceInfo):
        # udid 가 일치하지 않으면 예외
        if driver.capabilities['udid'] != device_info.udid:
            raise ValueError('app_driver does not match device_info', driver, device_info)
