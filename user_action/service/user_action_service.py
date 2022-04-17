from sql_alchemy.domain.sql_alchemy import session
from user_action.domain.user import User
from user_action.domain.user_action import UserAction


# 계정 행동 양식 생성
def insert_user_action(user: User, user_action: UserAction):
    # 계정, 행동 연결
    user_action.user_seq = user.user_seq
    # 저장
    session.add(user_action)
    session.commit()
