import time

from one_dragon.utils.log_utils import get_logger

timers = {}
time_ticker_log = get_logger("time_ticker_log.txt", "time_ticker_log")

def log_and_tick(msg: str, tag: str = "default", clean_tick:bool=False):
    now = time.time_ns()
    if tag in timers and not clean_tick:
        start, last_tick = timers[tag]
    else:
        start, last_tick = (now, now)
    timers[tag] = (start, now)
    if not clean_tick:
        time_ticker_log.info(f"TimeLog {msg}, interval[{(now - last_tick) / 1000000}ms], total[{(now - start) / 1000000}ms]")
