from appium.domain.common.Platform_type import PlatformName


# appium 연결시 전달값
class DesiredCapabilities:
    # 핸드폰 OS
    platformName: PlatformName
    # 핸드폰 고유 번호
    uuid: str
