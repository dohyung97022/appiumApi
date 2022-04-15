from subprocess import Popen, PIPE


# subprocess 시작
def start(cmd: list[str]) -> Popen:
    return Popen(cmd, stdout=PIPE, stderr=PIPE)


# subprocess 출력을 반환
def read(subprocess: Popen) -> str:
    result = ''
    if is_finished(subprocess):
        lines = subprocess.stdout.readlines()
        for line in lines:
            result += line.decode('utf-8').strip() + '\n'
    else:
        results = subprocess.stdout.readlines()
        decoded_results = []
        for result in results:
            decoded_results.append(result.decode('utf-8').strip() + '\n')
        result = ''.join(decoded_results)
    return result


# subprocess 종료 여부를 반환
def is_finished(subprocess: Popen) -> bool:
    return subprocess.poll() is not None


# subprocess 끝날 때까지 대기
def wait_until_finished(subprocess: Popen):
    while not is_finished(subprocess):
        continue


# subprocess 종료
def kill(subprocess: Popen):
    subprocess.terminate()
    subprocess.kill()


# subprocess 모두 종료
def kill_all(subprocesses: list[Popen]):
    for subprocess in subprocesses:
        kill(subprocess)
