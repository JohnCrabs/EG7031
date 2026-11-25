from enum import Enum
from PythonExamples.AY_2026_2027.Ex01.calendar import *


class MSG_TYPE(Enum):
    DEFAULT = "default"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


def p_msg(msg: str, m_type: MSG_TYPE = MSG_TYPE.DEFAULT):
    if m_type == MSG_TYPE.INFO:
        print(f"{currTime()}::INFO::{msg}")
    elif m_type == MSG_TYPE.WARNING:
        print(f"{currTime()}::WARNING::{msg}")
    elif m_type == MSG_TYPE.ERROR:
        print(f"{currTime()}::ERROR::{msg}")
    else:
        print(f"{currTime()}::{msg}")


class Log:
    def __init__(self, path: str or None = None):
        self.__logPath__ = None
        self.lPath = path

    @property
    def lPath(self):
        return self.__logPath__

    @lPath.setter
    def lPath(self, path: str):
        if type(path) is str:
            self.__logPath__ = path
        else:
            p_msg('Given "path" parameter is not str. lPath has not changed!', MSG_TYPE.WARNING)

    def createFile(self):
        pass

    def addMessage(self):
        pass


if __name__ == "__main__":
    # p_msg("Hello World!", MSG_TYPE.INFO)
    # p_msg("Hello World!", MSG_TYPE.WARNING)
    # p_msg("Hello World!", MSG_TYPE.ERROR)
    # p_msg("Hello World!")

    logFile = Log(path="4646464646")
    if logFile.lPath:
        print(f"{logFile.lPath}")
    else:
        logFile.lPath = "myAwesomePath"
        print(f"{logFile.lPath}")
    print(f"Final: {logFile.lPath}")

