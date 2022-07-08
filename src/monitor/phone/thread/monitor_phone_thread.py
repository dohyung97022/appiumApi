from src.appium_api.service.appium_device_service import get_screenshot_base64, get_app_driver
from src.flask_socket_io.domain.flask_socket_io import socketio
from src.utils.img_service import resize_base_64
from src import config


# 모든 디바이스 화면 받기
def monitor_phone_socket_job(devices):

    # udid
    udid = devices.device_info.udid
    try:

        # 스크린샷
        screenshot = get_screenshot_base64(devices.app_driver)

        # 단일 화면 전송
        socketio.emit(
            'phone_screen_connect',
            {
                'img':
                    'data:image/png;base64,' +
                    resize_base_64(screenshot, 300, 500),
                'udid': udid
            },
            room=udid
        )

        # 화면 모음 전송
        socketio.emit(
            'phone_screens_connect',
            {
                'img':
                    'data:image/png;base64,' +
                    resize_base_64(screenshot, 150, 250),
                'udid': udid
            },
            room='phone_screens'
        )

    except:
        print('phone_screen_connect exception')
        config.udid_to_device[udid].app_driver = get_app_driver(
            config.udid_to_device[udid].device_info)
