# appium_api 연결시 전달값
from src.utils.string_service import snake_case_to_camel_case


class DesiredCapabilities:
    # 핸드폰 고유 번호
    udid: str
    # 핸드폰 OS (Android / IOS)
    # TODO : Android 가 아닌 경우도 자동 절차로 받게끔 만들기
    platform_name: str
    # 크롬 자동화 드라이버
    chromedriver_executable: str
    # 브라우저 명
    browser_name: str

    def __init__(self, udid: str, platform_name='Android', browser_name='Chrome'):
        self.udid = udid
        self.platform_name = platform_name
        self.browser_name = browser_name

    def to_map(self):
        map = {}
        for key in vars(self):
            if vars(self)[key] is not None:
                map[snake_case_to_camel_case(key)] = vars(self)[key]
        return map
