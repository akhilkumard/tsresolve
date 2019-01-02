from tsresolve.event_parser import RecurringEvent
from tsresolve.time_stamp_resolver import point_of_time, period_of_time

def parse(s, now=None):
    return RecurringEvent(now).parse(s)

