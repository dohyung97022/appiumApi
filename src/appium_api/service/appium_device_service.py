from os import getcwd
from appium import webdriver
from src.appium_api.domain.common.package_name import PackageName
from src.appium_api.domain.desired_capabilities import DesiredCapabilities
from appium.webdriver.webdriver import WebDriver
from src.chrome_driver.service.chrome_driver_service import get_driver_location_of_base_version
from src.sub_process.domain.adb.device_info import DeviceInfo
from src.sub_process.service.subprocess_adb_service import get_app_version, get_base_app_version

# local appium 서버
appium_server = 'http://127.0.0.1:4723/wd/hub'


# 요청 값을 통해 driver 를 추출
def get_driver(desired_capabilities: DesiredCapabilities):
    return webdriver.Remote(appium_server, desired_capabilities.to_map())


# 디바이스 정보에서 chrome driver 추출
def get_chrome_driver(device_info: DeviceInfo):
    desired_capabilities = device_info.to_browser_desired_capabilities()
    chrome_version = get_app_version(device_info, PackageName.chrome.value)
    base_chrome_version = get_base_app_version(chrome_version)
    desired_capabilities.chromedriver_executable = get_driver_location_of_base_version(base_chrome_version)
    return get_driver(desired_capabilities)


# 디바이스 정보들에서 chrome drivers 추출
def get_chrome_drivers(device_infos: list[DeviceInfo]) -> list[WebDriver]:
    chrome_drivers = []

    for device_info in device_infos:
        chrome_drivers.append(get_chrome_driver(device_info))

    return chrome_drivers


# 디바이스 정보에서 app driver 추출
def get_app_driver(device_info: DeviceInfo) -> WebDriver:
    desired_capabilities = device_info.to_app_desired_capabilities()
    return get_driver(desired_capabilities)


# 디바이스 정보들에서 app drivers 추출
def get_app_drivers(device_infos: list[DeviceInfo]) -> list[WebDriver]:
    app_drivers = []

    for device_info in device_infos:
        app_drivers.append(get_app_driver(device_info))

    return app_drivers


# 화면 스크린샷 저장
def get_screenshot(app_driver: WebDriver):
    app_driver.save_screenshot(getcwd() + '/src/appium_api/screenshots/screenshot.png')


# 화면 스크린샷 base64 출력
def get_screenshot_base64(app_driver: WebDriver):
    return app_driver.get_screenshot_as_base64()
