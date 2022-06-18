from src.sub_process.domain.adb.device_info import DeviceInfo


class AdbCommands:
    # adb 에 연결된 기기의 id 와 연결 상태 반환
    get_all_devices: list[str] = ['adb', 'devices']

    # 앱의 버전 반환
    @classmethod
    def get_app_version(cls, device_info: DeviceInfo, package_name: str) -> list[str]:
        return ['adb', '-s', device_info.udid, 'shell', 'dumpsys', 'package', package_name, '|', 'grep', 'versionName']

    # 디바이스 화면 크기 반환
    @classmethod
    def get_device_size(cls, device_udid: str) -> list[str]:
        return ['adb', '-s', device_udid, 'shell', 'wm', 'size']

    # 디바이스 터치
    @classmethod
    def touch_screen(cls, device_info: DeviceInfo, x: int, y: int) -> list[str]:
        return ['adb', '-s', device_info.udid, 'shell', 'input', 'touchscreen', 'tap', str(x), str(y)]