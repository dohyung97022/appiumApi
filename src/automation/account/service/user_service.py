import string
import random

from faker import Faker

from src.sql_alchemy.domain.sql_alchemy import session
from src.automation.account.common.faker_locale import FakerLocale
from src.sql_alchemy.db_model.account import Account


# 계정 저장
def insert_user(user: Account):
    session.add(user)
    session.commit()


# 계정 선택
def select_user_by_seq(seq: int) -> Account:
    return session.query(Account).get(seq)


# 랜덤 가입용 계정 생성
def generate_random_user(udid: str, email_postfix: str, site: str, locale: FakerLocale = FakerLocale.KR):
    fake = Faker(locale=locale.value)
    profile = fake.simple_profile()
    profile['username'] = profile['username'] + generate_random_number_string()
    password = generate_random_string()

    return Account(profile['username'] + email_postfix, password, udid, site, profile)


# 12자리의 숫자 생성
def generate_random_number_string(size=5):
    return generate_random_string(size=size, chars=string.digits)


# 12자리의 숫자 + 소문자 + 대문자 생성
def generate_random_string(size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
