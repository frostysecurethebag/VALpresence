import time
from datetime import datetime
from dateutil import tz



def get_time(timer):
    pattern = '%Y.%m.%d-%H.%M.%S'
    gg=datetime.strptime(timer, pattern)
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    gg = gg.replace(tzinfo=from_zone)
    oof = gg.astimezone(to_zone)
    x=str(oof)
    x=x.split("+")
    new_pattern="%Y-%m-%d %H:%M:%S"
    starto= int(time.mktime(time.strptime(x[0], new_pattern)))
    return starto