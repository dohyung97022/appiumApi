import src.setup  # 기본 setup

from src.flask_socket_io.domain.flask_socket_io import socketio, app
from src.sb.service import sb_service
from src.automation.service import user_service
from src.appium_api.service import appium_device_service
from src.config import current_devices


def example_appium():
    # 디바이스
    device = list(current_devices.udid_to_devices.values())[0]

    # 크롬 / 앱 드라이버 가져오기
    chrome_driver = device.web_driver
    app_driver = device.app_driver

    appium_device_service.get_screenshot(app_driver)

    # s3 파일을 url 을 만들기
    # url = generate_presigned_url(S3GeneratePresignedUrlReq('appiumapi', 'file_example_MP4_480_1_5MG.mp4'))
    # 디바이스 안에서 다운로드 받기
    # download_url(url, chrome_driver, app_driver)
    # sb 들어가기
    sb_service.goto_sb(chrome_driver)
    # 회원 조회
    user = user_service.select_user_by_seq(3)
    # sb 로그인하기
    sb_service.login_sb(chrome_driver, user)
    # sb 업로드하기
    sb_service.upload_video(chrome_driver)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8082)
