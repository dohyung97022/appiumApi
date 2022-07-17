from src.appium_api.service import appium_device_run_service
from src.automation.action.service import action_service
from src.automation.phone.model.get_action_run_req import GetActionRunReq
from src.config import udid_to_device


def phone_action_appium_run(req: GetActionRunReq):
    # action 조회
    action = action_service.select_action(req.action_seq)

    # 테스트, 재연결
    appium_device_run_service.test_and_reconnect_driver_session(udid_to_device[req.udid])

    # action 실행
    appium_device_run_service.run_action(udid_to_device[req.udid], action)

    return
