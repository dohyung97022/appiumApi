from os import getcwd
from appium import webdriver
from src.appium_api.domain.common.package_name import PackageName
from src.appium_api.domain.desired_capabilities import DesiredCapabilities
from appium.webdriver.webdriver import WebDriver
from src.appium_api.domain.device import Device
from src.chrome_driver.service.chrome_driver_service import get_driver_location_of_base_version
from src.sub_process.domain.adb.device_info import DeviceInfo
from src.sub_process.service.subprocess_adb_service import get_app_version, get_base_app_version

# local appium 서버
appium_server: str = 'http://127.0.0.1'
appium_path: str = '/wd/hub'


# 디바이스 연결
# chrome, app 동시 접속은 안된다.
def connect_device(device_info: DeviceInfo) -> Device:
    app_driver = get_app_driver(device_info)
    chrome_driver = get_chrome_driver(device_info)
    return Device(device_info, app_driver, chrome_driver)


# 요청 값을 통해 driver 를 추출
def get_driver(desired_capabilities: DesiredCapabilities):
    return webdriver.Remote(
        appium_server + ':' + str(desired_capabilities.port) + appium_path,
        desired_capabilities.to_map()
    )


# 디바이스 정보에서 chrome driver 추출
def get_chrome_driver(device_info: DeviceInfo):
    desired_capabilities = device_info.to_browser_desired_capabilities()
    chrome_version = get_app_version(device_info, PackageName.chrome.value)
    base_chrome_version = get_base_app_version(chrome_version)
    desired_capabilities.chromedriver_executable = get_driver_location_of_base_version(base_chrome_version)
    return get_driver(desired_capabilities)


# 디바이스 정보에서 app driver 추출
def get_app_driver(device_info: DeviceInfo) -> WebDriver:
    desired_capabilities = device_info.to_app_desired_capabilities()
    return get_driver(desired_capabilities)


# 화면 스크린샷 저장
def get_screenshot(app_driver: WebDriver):
    app_driver.save_screenshot(getcwd() + '/src/appium_api/screenshots/screenshot.png')
