from sub_process.domain.adb.device_info import DeviceInfo


class AdbCommands:
    # adb 에 연결된 기기의 id 와 연결 상태 반환
    get_all_devices: list[str] = ['adb', 'devices']

    # 앱의 버전 반환
    @classmethod
    def get_app_version(cls, device_info: DeviceInfo, package_name: str) -> list[str]:
        return ['adb', '-s', device_info.uuid, 'shell', 'dumpsys', 'package', package_name, '|', 'grep', 'versionName']
