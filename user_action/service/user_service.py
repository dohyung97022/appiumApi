from sql_alchemy.domain.sql_alchemy import session
from user_action.domain.user import User


# 계정 생성
def insert_user(user: User):
    session.add(user)
    session.commit()
