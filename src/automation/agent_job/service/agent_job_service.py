import time
from src.appium_api.domain.device import Device
from src.automation.agent_job.model.assign_job_to_agent_req import AssignJobToAgentReq
from src.sql_alchemy.db_model.agent import Agent
from src.sql_alchemy.db_model.macro import Macro
from src.sql_alchemy.domain.sql_alchemy import session

job_to_udids_to_agents: dict[str, dict[str, Agent | None]] = {}


# 추가
def add_job_udid(job: str, udid: str):
    global job_to_udids_to_agents
    # 없을 경우
    if job not in job_to_udids_to_agents:
        job_to_udids_to_agents[job] = {}
    # 요원 할당 안됨
    job_to_udids_to_agents[job][udid] = None


# 할당
def assign_job_to_agent(req: AssignJobToAgentReq):
    global job_to_udids_to_agents

    # agent 조회
    agent = session.query(Agent) \
        .filter(Agent.agent_email == req.agent_email) \
        .first()

    if req.job not in job_to_udids_to_agents:
        return None

    for udid in job_to_udids_to_agents[req.job]:
        # 비어있는 udid 확인
        if job_to_udids_to_agents[req.job][udid] is None:
            # 요원 할당
            job_to_udids_to_agents[req.job][udid] = agent
            return udid

    return None


# 수행 완료 대기
def wait_job_udid(device: Device, macro: Macro, job: str, max_sec: int):
    global job_to_udids_to_agents

    for i in range(int(max_sec)):

        # 작업 완료될 경우
        if device.device_info.udid not in job_to_udids_to_agents[job]:
            return

        # 작업 완료 element 찾기
        elements = device.web_driver.find_elements(macro.element_type.to_appium_by(), macro.element)

        # 작업 완료
        if len(elements) > 0:
            job_to_udids_to_agents[job][device.device_info.udid].is_job_finished = True
            # 화면 없어질 때까지 대기
            time.sleep(3)
            return

        # 대기
        time.sleep(1)

    return


# 이전 작업이 완료된 경우 계정 저장
def save_account_if_finish_job(device: Device, job: str):
    agent = job_to_udids_to_agents[job][device.device_info.udid]
    # agent 이 할당되지 않은 경우
    if agent is None:
        return
    # agent 가 작업을 끝낸 경우
    if agent.is_job_finished is True:
        session.add(device.account)
        session.commit()


# 수행 완료 / 시간 초과
def finish_job_udid(job: str, udid: str):
    global job_to_udids_to_agents
    if udid in job_to_udids_to_agents[job]:
        job_to_udids_to_agents[job].pop(udid)


# udid 의 agents 반환
def get_assigned_agent_of_udid(udid: str) -> Agent | None:
    global job_to_udids_to_agents

    for job in job_to_udids_to_agents:
        if udid in job_to_udids_to_agents[job] and job_to_udids_to_agents[job][udid] is not None:
            return job_to_udids_to_agents[job][udid]

    return None
