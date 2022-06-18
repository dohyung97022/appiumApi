import string
import random

from faker import Faker

from src.sql_alchemy.domain.sql_alchemy import session
from src.automation.domain.common.faker_locale import FakerLocale
from src.automation.domain.user import User


# 계정 저장
def insert_user(user: User):
    session.add(user)
    session.commit()


# 계정 선택
def select_user_by_seq(seq: int) -> User:
    return session.query(User).get(seq)


# 랜덤 가입용 계정 생성
def generate_random_user(email: str, udid: str, site: str, locale: FakerLocale = FakerLocale.KR):
    fake = Faker(locale=locale.value)
    profile = fake.simple_profile()
    password = generate_random_string()

    return User(email, password, udid, site, profile)


# 12자리의 숫자 + 소문자 + 대문자 생성
def generate_random_string(size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))