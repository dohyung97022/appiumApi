from src.appium_api.domain.device import Device
from src.sql_alchemy.db_model.phone import Phone
from src.sql_alchemy.domain.sql_alchemy import session


def insert_phones(udid_to_device: dict[str, Device]):
    # device -> phone 전환
    phones = list(map(lambda device: Phone(device), list(udid_to_device.values())))
    # 입력
    for phone in phones:
        session.merge(phone)
    # 커밋
    session.commit()
