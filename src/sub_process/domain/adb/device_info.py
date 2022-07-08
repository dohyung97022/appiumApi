from src.appium_api.domain.desired_capabilities import DesiredCapabilities


class DeviceInfo:
    # 기기 고유 번호
    udid: str
    # 기기 연결 상태
    # TODO : 모든 상태값이 규정된 이후 enum 으로 빼내기
    state: str
    # appium 포트번호
    port: int
    # 기기 넓이
    width: int
    # 기기 높이
    height: int

    def __init__(self, udid: str, state: str, port: int, width: int, height: int):
        self.udid = udid
        self.state = state
        self.port = port
        self.width = width
        self.height = height

    def to_browser_desired_capabilities(self):
        return DesiredCapabilities(self.udid, self.port)

    def to_app_desired_capabilities(self):
        return DesiredCapabilities(self.udid, self.port, browser_name=None)
