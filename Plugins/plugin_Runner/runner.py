import os
import signal
from multiprocessing import Process

def run(target, *args, **kwargs):
    print("[#] Start Runner")
    proc = Process(target=target, args=args, kwargs=kwargs)
    proc.start()
    return proc.pid

def stop(pid: int):
    print("[#] Stop Runner")
    os.kill(pid, signal.SIGTERM)