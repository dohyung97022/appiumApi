from src.sub_process.service.subprocess_adb_service import touch_screen
from src import config


def phone_touch(req):

    # udid 로 디바이스 찾기
    device = config.udid_to_device.get(req['udid'])

    # 터치된 위치의 비율
    x_portion = req['touch_x'] / req['touch_w']
    y_portion = req['touch_y'] / req['touch_h']

    # 터치된 위치
    touch_x = device.device_info.width * x_portion
    touch_y = device.device_info.height * y_portion

    # 디바이스 터치
    touch_screen(device.device_info, touch_x, touch_y)
