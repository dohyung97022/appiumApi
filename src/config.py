import os
import subprocess

from src.appium_api.domain.current_deivces import CurrentDevices
from src.appium_api.service.appium_device_service import get_app_drivers, get_chrome_drivers
from src.sub_process.service.subprocess_adb_service import get_all_adb_device_info
from src.sql_alchemy.domain.sql_alchemy import db_setup

# global 설정
device_infos = None
app_drivers = None
web_drivers = None
current_devices = None


# 모든 app_driver, web_driver 설정
def appium_config():
    global device_infos
    global app_drivers
    global web_drivers
    global current_devices

    device_infos = get_all_adb_device_info()
    app_drivers = get_app_drivers(device_infos)
    web_drivers = get_chrome_drivers(device_infos)
    current_devices = CurrentDevices(device_infos, app_drivers, web_drivers)


def npm_config():
    subprocess.Popen(['vue', 'serve'], cwd=os.getcwd() + '/templates')


def db_config():
    db_setup()  # sql alchemy 데이터베이스 생성
