from src.appium_api.service.appium_device_service import get_screenshot_base64, get_app_driver
from src.flask_socket_io.domain.flask_socket_io import socketio
from src.utils.img_service import resize_base_64
from src.utils.thread_service import ThreadJob
from src.config import current_devices


# 모든 디바이스 화면 받기
def monitor_phone_socket_job():

    # 화면 모음
    phone_screens = []

    # 모든 디바이스
    for devices in list(current_devices.udid_to_devices.values()):

        # udid
        udid = devices.device_info.udid

        try:
            # 스크린샷
            screenshot = get_screenshot_base64(devices.app_driver)

            # 화면 모음에 추가
            phone_screens.append({
                'img':
                    'data:image/png;base64,' +
                    resize_base_64(screenshot, 150, 250),
                'udid': udid
            })

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
        except:
            print('phone_screen_connect exception')
            current_devices.udid_to_devices[udid].app_driver = get_app_driver(
                current_devices.udid_to_devices[udid].device_info)

    try:
        # 화면 모음 전송
        socketio.emit(
            'phone_screens_connect',
            phone_screens,
            room='phone_screens'
        )
    except:
        print('phone_screens_connect exception')


# thread 로 디바이스 화면 모음 전송
thread_job = ThreadJob(
    method=monitor_phone_socket_job,
    method_args=[],
    interval=0.5
)
thread_job.start()
