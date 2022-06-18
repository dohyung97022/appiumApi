import threading

event = threading.Event()


# 해당 function 을 반복한다.
class ThreadJob(threading.Thread):
    def __init__(self, method, method_args, interval: float, *args, **kwargs):
        self.method = method
        self.method_args = method_args
        self.event = event
        self.interval = interval
        super(ThreadJob, self).__init__(target=method, *args, **kwargs)

    def run(self):
        while not self.event.wait(self.interval):
            self.method(*self.method_args)
