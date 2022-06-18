from src.sql_alchemy.domain.sql_alchemy import session
from src.automation.domain.common.epoch import epoch_datetime
from src.automation.domain.user import User
from src.automation.domain.user_action import UserAction
from datetime import datetime


# 계정 행동 양식 생성
def insert_user_action(user: User, user_action: UserAction):
    # 계정, 행동 연결
    user_action.user_seq = user.user_seq
    # 저장
    session.add(user_action)
    session.commit()


# 행동 순환 시간이 지난 행동 반환
def select_user_action_over_cycle_time() -> list[UserAction]:
    user_actions = list[UserAction](session.query(UserAction).all())

    # TODO : sql 문으로 해결할 필터를 걸 수 있게 변경
    def filter_over_cycle_time(user_action: UserAction):
        interval = datetime.now() - user_action.last_action_date
        wait_time = user_action.cycle_time - epoch_datetime
        return interval > wait_time

    return list[UserAction](filter(filter_over_cycle_time, user_actions))
