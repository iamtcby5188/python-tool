import time
import uuid

__all__ = ['getUUID', 'getCurrentTime']


def getUUID() -> str:
    return str(uuid.uuid1())


def getCurrentTime() -> float:
    return time.time()
