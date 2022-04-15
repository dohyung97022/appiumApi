from sub_process.domain.adb.adb_commands import AdbCommands
from sub_process.domain.adb.device_info import DeviceInfo
from sub_process.service.subprocess_service import start, read, kill
import re


def get_all_adb_device_info():
    # subprocess 시작
    poppen = start(AdbCommands.get_all_devices)
    # subprocess 읽기
    info = read(poppen)
    # regex 로 정보 추출
    device_uuids = re.findall('\n([^\s]*)\t', info)
    device_states = re.findall('\n[^\s]*\t([^\s]*)', info)
    # 타입에 주입
    device_infos : list[DeviceInfo] = []
    for i in range(len(device_uuids)):
        device_info = DeviceInfo(device_uuids[i], device_states[i])
        device_infos.append(device_info)
    # subprocess 연결 해제
    kill(poppen)
    # 반환
    return device_infos
