from src.automation.agent_job.service import agent_job_service
from src.flask_socket_io.domain.flask_socket_io import socketio
from src.sub_process.service import subprocess_adb_service
from src.utils.img_service import resize_base_64


# 모든 디바이스 화면 받기
def monitor_phone_socket_job(device):

    # udid
    udid = device.device_info.udid
    try:

        # 스크린샷
        screenshot = subprocess_adb_service.get_screen_base64(device.device_info)
        big_screenshot = resize_base_64(screenshot, 300, 500)
        small_screenshot = resize_base_64(screenshot, 150, 250)

        # 단일 화면 전송
        socketio.emit(
            'phone_screen_connect',
            {
                'img':
                    'data:image/png;base64,' +
                    big_screenshot,
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
                    small_screenshot,
                'udid': udid
            },
            room='phone_screens'
        )

        # agent 화면 전송
        agent = agent_job_service.get_assigned_agent_of_udid(udid)

        if agent is not None:
            if agent.is_job_finished:
                big_screenshot = ''

            socketio.emit(
                'phone_screen_connect',
                {
                    'img':
                        'data:image/png;base64,' +
                        big_screenshot,
                    'udid': udid
                },
                room=agent.agent_email
            )

    except Exception as e:
        print(e)
