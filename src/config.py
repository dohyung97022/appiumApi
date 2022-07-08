import os
import subprocess
import threading
import time

from src.appium_api.domain.device import Device
from src.monitor.phone.thread.monitor_phone_thread import monitor_phone_socket_job
from src.sub_process.domain.adb.device_info import DeviceInfo
from src.sub_process.service import subprocess_adb_service
from src.sql_alchemy.domain.sql_alchemy import db_setup
from src.appium_api.service import appium_device_service
from src.utils.thread_service import ThreadJob

udid_to_device: dict[str, Device] = {}


# 모든 기기 연결
def appium_config():
    subprocess.Popen(['pkill', '-9', 'appium'])

    # adb 기기 정보
    device_infos = subprocess_adb_service.get_all_adb_device_info()

    for device_info in device_infos:
        subprocess.Popen(['appium', '-p', str(device_info.port), '--log-level', 'error'])

    time.sleep(5)

    threads = []
    for device_info in device_infos:
        t = threading.Thread(target=device_config, args=(device_info,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


def device_config(device_info: DeviceInfo):
    global udid_to_device
    device = appium_device_service.connect_device(device_info)
    udid_to_device[device.device_info.udid] = device


def thread_config():
    # 모든 디바이스
    for devices in list(udid_to_device.values()):
        # thread 로 디바이스 화면 모음 전송
        thread_job = ThreadJob(
            method=monitor_phone_socket_job,
            method_args=[devices],
            interval=0.5
        )
        thread_job.start()


def npm_config():
    subprocess.Popen(['vue', 'serve'], cwd=os.getcwd() + '/templates')


def db_config():
    db_setup()  # sql alchemy 데이터베이스 생성
