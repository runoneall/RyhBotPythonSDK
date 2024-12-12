from multiprocessing import Process

proc: Process = None

def run(target, *args, **kwargs):
    global proc
    print("--- Code Running In Runner ---")
    proc = Process(target=target, args=args, kwargs=kwargs)
    proc.start()

def stop():
    global proc
    print("--- Stopping Runner ---")
    if proc is not None and proc.is_alive():
        proc.terminate()
        proc.join()
        proc = None
    print("--- Runner Stopped ---")