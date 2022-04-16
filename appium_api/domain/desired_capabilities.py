# appium_api 연결시 전달값
class DesiredCapabilities:
    # 핸드폰 고유 번호
    uuid: str
    # 핸드폰 OS (Android / IOS)
    # TODO : Android 가 아닌 경우도 자동 절차로 받게끔 만들기
    platform_name: str = 'Android'
    # 크롬 자동화 드라이버
    chrome_driver_executable: str
    # 브라우저 명
    browser_name: str = 'Chrome'

    def __init__(self, uuid: str):
        self.uuid = uuid

    def to_map(self):
        return {
            'uuid': self.uuid,
            'platformName': self.platform_name,
            'chromedriverExecutable': self.chrome_driver_executable,
            'browserName': self.browser_name
        }
