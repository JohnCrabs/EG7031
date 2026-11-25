import datetime as dt


# Return datetime in format "%Y/%m/%dT%H:%M:%S"
def currTime():
    return dt.datetime.now().strftime("%Y/%m/%dT%H:%M:%S")


if __name__ == "__main__":
    print(currTime())
