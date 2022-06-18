from src.automation.domain.macro import Macro
from src.sql_alchemy.domain.sql_alchemy import session


# 모든 매크로 선택
def select_macros() -> list[Macro]:
    return list[Macro](session.query(Macro).all())


# 매크로 저장
def insert_macro(macro: Macro):
    session.add(macro)
    session.commit()
