from src.sub_process.domain.adb.adb_commands import AdbCommands
from src.sub_process.domain.adb.device_info import DeviceInfo
from src.sub_process.service.subprocess_service import start, read, kill
import re

appium_port: int = 4000


# 연결된 모든 기기의 정보 반환
def get_all_adb_device_info() -> list[DeviceInfo]:
    global appium_port
    # subprocess 시작
    popen = start(AdbCommands.get_all_devices)
    # subprocess 읽기
    info = read(popen)
    # regex 로 정보 추출
    device_udids = re.findall('\n([^\s]*)\t', info)
    device_states = re.findall('\n[^\s]*\t([^\s]*)', info)
    # 타입에 주입
    device_infos: list[DeviceInfo] = []
    for i in range(len(device_udids)):
        width, height = get_device_size(device_udids[i])
        device_info = DeviceInfo(device_udids[i], device_states[i], appium_port, width, height)
        device_infos.append(device_info)
        appium_port = appium_port + 1
    # subprocess 연결 해제
    kill(popen)
    # 반환
    return device_infos


# package_name 의 앱 버전을 반환
def get_app_version(device_info: DeviceInfo, package_name: str):
    # subprocess 시작
    popen = start(AdbCommands.get_app_version(device_info, package_name))
    info = read(popen)
    kill(popen)
    # regex 로 정보 추출
    return re.findall('versionName=([^\s]*)', info)[0]


# 버전에서 base 반환
def get_base_app_version(app_version: str):
    return re.findall('([^\s]*)\.[^\s]*\.[^\s]*\.', app_version)[0]


# 디바이스 사이즈를 반환
def get_device_size(device_udid: str) -> tuple[int, int]:
    # subprocess 시작
    popen = start(AdbCommands.get_device_size(device_udid))
    info = read(popen)
    kill(popen)
    # regex 로 widthxheight 반환
    info = re.findall('size: ([^\s]*)\\n', info)[0]
    # partition 으로 전후 추출
    width, keyword, height = info.partition('x')
    # 기기 정보 지정
    return int(width), int(height)


# 디바이스 터치
def touch_screen(device_info: DeviceInfo, x: int, y: int):
    # subprocess 시작
    popen = start(AdbCommands.touch_screen(device_info, x, y))
    info = read(popen)
    kill(popen)
