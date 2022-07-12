
from xmlrpc.client import Boolean


def overlap(start_time, end_time, time) -> Boolean:
    """
    Check if new time is inside time interval
    """
    if start_time < time > end_time:
        return True
    return False
