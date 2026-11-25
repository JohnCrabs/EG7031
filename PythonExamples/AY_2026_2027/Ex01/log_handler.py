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


if __name__ == "__main__":
    p_msg("Hello World!", MSG_TYPE.INFO)
    p_msg("Hello World!", MSG_TYPE.WARNING)
    p_msg("Hello World!", MSG_TYPE.ERROR)
    p_msg("Hello World!")
