from src.appium_api.domain.device import Device
from src.automation.account.service import user_service
from src.automation.agent_job.service import agent_job_service
from src.sql_alchemy.db_model.macro import Macro


# TODO : device, macro element 등을 클래스로 받기
def open_url(device: Device, macro: Macro, element, url: str):
    device.web_driver.get(url)


def set_new_account(device: Device, macro: Macro, element, email_postfix: str, url: str):
    device.account = user_service.generate_random_user(device.device_info.udid, email_postfix, url)


def type_account_username(device: Device, macro: Macro, element):
    element.send_keys(device.account.username)


def type_account_password(device: Device, macro: Macro, element):
    element.send_keys(device.account.account_pw)


def type_account_firstname(device: Device, macro: Macro, element):
    element.send_keys(device.account.name[0])


def type_account_lastname(device: Device, macro: Macro, element):
    element.send_keys(device.account.name[1:])


def type_account_year(device: Device, macro: Macro, element):
    element.send_keys(str(device.account.birthdate.year))


def type_account_month(device: Device, macro: Macro, element):
    element.send_keys(str(device.account.birthdate.month))


def type_account_day(device: Device, macro: Macro, element):
    element.send_keys(str(device.account.birthdate.day))


def request_agent_job(device: Device, macro: Macro, element, job: str):
    agent_job_service.add_job_udid(job, device.device_info.udid)


def wait_agent_job(device: Device, macro: Macro, element, job: str, max_sec: str):
    agent_job_service.wait_job_udid(device, macro, job, int(max_sec))


def save_account_if_finish_job(device: Device, macro: Macro, element, job):
    agent_job_service.save_account_if_finish_job(device, job)


def finish_agent_job(device: Device, macro: Macro, element, job: str):
    agent_job_service.finish_job_udid(job, device.device_info.udid)
