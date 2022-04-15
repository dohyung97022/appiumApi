from appium_api.domain.desired_capabilities import DesiredCapabilities


class DeviceInfo:
    # 기기 고유 번호
    uuid: str
    # 기기 연결 상태
    # TODO : 모든 상태값이 규정된 이후 enum 으로 빼내기
    state: str

    def __init__(self, uuid: str, state: str):
        self.uuid = uuid
        self.state = state

    def to_desired_capabilities(self):
        return DesiredCapabilities(self.uuid)
