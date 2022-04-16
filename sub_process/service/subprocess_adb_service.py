from sub_process.domain.adb.adb_commands import AdbCommands
from sub_process.domain.adb.device_info import DeviceInfo
from sub_process.service.subprocess_service import start, read, kill
import re


# 연결된 모든 기기의 정보 반환
def get_all_adb_device_info():
    # subprocess 시작
    popen = start(AdbCommands.get_all_devices)
    # subprocess 읽기
    info = read(popen)
    # regex 로 정보 추출
    device_uuids = re.findall('\n([^\s]*)\t', info)
    device_states = re.findall('\n[^\s]*\t([^\s]*)', info)
    # 타입에 주입
    device_infos: list[DeviceInfo] = []
    for i in range(len(device_uuids)):
        device_info = DeviceInfo(device_uuids[i], device_states[i])
        device_infos.append(device_info)
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