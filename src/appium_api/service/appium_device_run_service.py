import random
import time

from selenium.webdriver.common.by import By
from src.appium_api.domain.device import Device
from src.sql_alchemy.db_model.action import Action
from src.sql_alchemy.db_model.macro import Macro, MacroType, MacroOperator
from src.appium_api.service import appium_device_run_code_service, appium_device_service
from src.sql_alchemy.db_model.phone import Phone
from src.sql_alchemy.db_model.phone_action_association import LoopType
from src.sql_alchemy.domain.sql_alchemy import session
from src.sub_process.service import subprocess_adb_service


# action 을 thread 로서 돌림
def run_actions_thread(device: Device):

    # 해당 핸드폰에 할당된 모든 action
    phone = session.query(Phone) \
        .filter(Phone.udid == device.device_info.udid) \
        .first()

    for action_association in phone.action_associations:

        # 돌 루프가 없을 경우
        if action_association.current_loop == 0:
            return

        # 루프 소비
        action_association.current_loop = action_association.current_loop - 1
        session.commit()

        # 화면 켜기
        subprocess_adb_service.wakeup(device.device_info)

        # 잠금 해제
        subprocess_adb_service.unlock(device.device_info)

        # 테스트, 재연결
        test_and_reconnect_driver_session(device)

        # TODO : 단일루프, 일간루프 기능 구현

        # 단일 루프
        if action_association.loop_type is LoopType.SINGLE_USE:
            run_action(device, action_association.action)

        # 일간 루프
        if action_association.loop_type is LoopType.DAILY:
            run_action(device, action_association.action)


def run_action(device: Device, action: Action):
    # or 일 경우 취합 후 결정
    or_macro = []

    # 매크로 실행
    for i in range(len(action.macros)):

        macro: Macro = action.macros[i]

        # or 일 경우
        if macro.macro_operator == MacroOperator.OR:
            or_macro.append(macro)

            # 다음 매크로가 없거나, or 가 아닐 경우
            if i + 1 >= len(action.macros) or action.macros[i + 1].macro_operator != MacroOperator.OR:
                # 지정
                macro = random.choice(or_macro)
                or_macro = []
            else:
                continue

        # 실행
        try:
            run_macro(device, macro)
        except Exception as e:
            # try 일 경우 오류 무시
            if macro.macro_operator == MacroOperator.TRY:
                continue
            raise e

    # 자식 action 재귀 실행
    for child_action_association in action.child_action_associations:
        run_action(device, child_action_association.child_action)

    return


def run_macro(device: Device, macro: Macro):
    # app / web 드라이버 설정
    driver = device.get_driver_of_type(macro.driver_type)

    # 키보드 숨김
    device.web_driver.hide_keyboard()

    element = None
    print(f'macro: {macro.name}\ntype: {macro.macro_type}\nelement: {macro.element}\n')
    if macro.element != '' and macro.element is not None:
        # elements 가져오기
        elements = driver.find_elements(macro.element_type.to_appium_by(), macro.element)

        # index 가 넘어갈 경우, run 일 경우 무시 가능
        if len(elements) <= macro.macro_index and macro.macro_type != MacroType.RUN:
            print(macro.to_dict())
            raise Exception("macro element index error.")

        # element 가져오기
        elif len(elements) > macro.macro_index:
            element = elements[macro.macro_index]

    # 코드 실행일 경우
    if macro.macro_type is MacroType.RUN: run_code(device, macro, element)
    if macro.macro_type is MacroType.CLICK: element.click()
    elif macro.macro_type is MacroType.TYPE: element.send_keys(macro.variable)

    # macro 시간 대기
    time.sleep(random.uniform(macro.min_wait_sec, macro.max_wait_sec))


def run_code(device: Device, macro: Macro, element):
    # 함수명, 변수 파싱
    variable = macro.variable.split('(')
    function_name = variable[0]
    variables = variable[1].replace(')', '').split(',')
    if variables == ['']: variables = []

    # function 가져오기
    code_function = getattr(appium_device_run_code_service, function_name)

    # function 실행
    code_function(device, macro, element, *variables)


def test_and_reconnect_driver_session(device: Device):
    # 연결 확인
    try:
        device.web_driver.find_elements(by=By.XPATH, value='test')
    except Exception as e:
        device.web_driver = appium_device_service.get_chrome_driver(device.device_info)

    try:
        device.app_driver.find_elements(by=By.XPATH, value='test')
    except Exception as e:
        device.app_driver = appium_device_service.get_app_driver(device.device_info)

    return device
