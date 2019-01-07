from tsresolve import RecurringEvent
from datetime import timedelta
from calendar import monthrange
import datetime
import re
from dateutil import parser
import logging

RE_DATES = re.compile(r'(?P<date>\d{1,2}st|\d{1,2}nd|\d{1,2}rd|\d{1,2}th)')
RE_YEAR = re.compile(r'(?P<year>\s\d{4})(\s|$)')
RE_AMMOD = re.compile(r'(?P<ammod>\sprevious|\sthis|\snext|\slast|\scoming|\supcoming)')
# This is to detect shortcut forms of months in future.
# RE_MONTH_NAMES = re.compile(r'(?P<ammod>previous|this|next|last|coming|upcoming)?\s(?P<month>jan(uary)?|'
#                             r'feb(r?uary)?|mar(ch)?|apr(il)?|may|jun(e)?|jul(y)?|aug(ust)?|sept?(ember)?|'
#                             r'oct(ober)?|nov(ember)?|dec(ember)?)\s?(?P<date>\d{1,2}st|\d{1,2}nd|'
#                             r'\d{1,2}rd|\d{1,2}th)?\s?(?P<year>\d{4})?')
RE_MONTH_NAMES = re.compile(
    r'(?P<ammod>previous|this|next|last|coming|upcoming)?\s(?P<month>january|february|march|april|'
    r'may|june|july|august|september|october|november|december)\s?'
    r'(?P<date>\d{1,2}st|\d{1,2}nd|\d{1,2}rd|\d{1,2}th)?\s?(?P<year>\d{4})?')
RE_DAYS = re.compile(
    r'%s?\s(?P<day>sunday|monday|tuesday|wednesday|thursday|friday|saturday|weekend)' % RE_AMMOD.pattern)
RE_TILL = re.compile(
    r'(?P<today>till\stoday|till\sdate|until\stoday|till\snow|till\stime|till\syesterday|till\stomorrow)')

logger = logging.getLogger("app_logger")


def point_of_time(phrase, NOW=""):
    try:
        NOW = parser.parse(NOW)
    except Exception as e:
        logger.error(e, exc_info=True)
        NOW = datetime.datetime.now()

    r = RecurringEvent(NOW)
    phrase = " " + phrase.lower()
    stamp, status = r.parse(phrase)

    if stamp is None:
        timestamp = None

    else:
        if status is False and "now" not in phrase:
            timestamp = stamp.replace(hour=9, minute=0, second=0, microsecond=0).isoformat()
        else:
            timestamp = stamp.isoformat()

    return timestamp, status


def period_of_time(phrase, NOW=""):
    try:
        NOW = parser.parse(NOW)
    except Exception as e:
        logger.error(e, exc_info=True)
        NOW = datetime.datetime.now()

    r = RecurringEvent(NOW)
    phrase = " " + phrase.lower()
    main_phrase_time = r.parse(phrase)

    if main_phrase_time[0] is None:
        ts, te = None, None
        return ts, te

    else:
        mphrase_time = main_phrase_time[0]
        monthname = RE_MONTH_NAMES.findall(phrase)
        dayname = RE_DAYS.findall(phrase)
        till_found = RE_TILL.findall(phrase)
        dates = RE_DATES.search(phrase)
        year_found = RE_YEAR.search(phrase)

        # Week calculates exactly 7 days in both the directions so resetting to week start and calculate next/last week
        if " week" in phrase and not monthname and "weekend" not in phrase:
            today_time = NOW
            week_day_number = NOW.weekday()
            this_week_start = today_time - timedelta(days=week_day_number)
            this_week_end = this_week_start + timedelta(days=5)

            if " last " in phrase or " previous " in phrase:
                last_week_start_day = this_week_start - timedelta(days=7)
                last_week_end_day = last_week_start_day + timedelta(days=5)

                ts, te = week_ts_te_generator(last_week_start_day, last_week_end_day)

            elif " next " in phrase:
                next_week_start_day = this_week_start + timedelta(days=7)
                next_week_end_day = next_week_start_day + timedelta(days=5)

                ts, te = week_ts_te_generator(next_week_start_day, next_week_end_day)

            else:
                this_week_start_day = this_week_start
                this_week_end_day = this_week_end

                ts, te = week_ts_te_generator(this_week_start_day, this_week_end_day)

        # This is to identify the month from given string and give result accordingly:
        elif monthname or " month" in phrase:
            phrase_time = year_handler(phrase, NOW)
            str_phrase_time = str(phrase_time)

            phrase_month_number = str_phrase_time.split("-")[1]
            phrase_year = str_phrase_time.split("-")[0]
            days_in_month = monthrange(int(phrase_year), int(phrase_month_number))[1]

            if len(monthname) > 1:
                m1 = " " + (' '.join(str(j) for j in monthname[0]))
                m2 = " " + (' '.join(str(k) for k in monthname[1]))
                mn = RE_DATES.search(m2)
                # checking ammod for string 2
                ammod_found_2 = RE_AMMOD.search(m2)

                phrase_time_1 = year_handler(m1, NOW)

                if ammod_found_2:
                    phrase_month_end = year_handler(m2, NOW)
                else:
                    phrase_time_2 = year_handler(m2, NOW)

                    if mn:
                        phrase_month_end = phrase_time_2
                    else:
                        phrase_month_number = str(phrase_time_2).split("-")[1]
                        phrase_year = str(phrase_time_2).split("-")[0]
                        days_in_month = monthrange(int(phrase_year), int(phrase_month_number))[1]
                        phrase_month_end = phrase_time_2 + timedelta(days=days_in_month - 1)

                ts, te = month_ts_te_generator(phrase_time_1, phrase_month_end)

            else:
                if till_found:
                    m1 = " " + (' '.join(str(j) for j in monthname[0]))
                    m2 = phrase.split("till")[1]

                    phrase_time_1 = year_handler(m1, NOW)
                    phrase_time_2 = r.parse(m2)[0]

                    if phrase_time_2 is None:
                        phrase_time_2 = NOW
                    else:
                        phrase_time_2 = year_handler(m2, NOW)

                    ts, te = month_ts_te_generator(phrase_time_1, phrase_time_2)

                elif dates:
                    phrase_time = year_handler(phrase, NOW)
                    ts, te = month_ts_te_generator(phrase_time, phrase_time)

                else:
                    phrase_month_start = phrase_time.replace(day=1)
                    phrase_month_end = phrase_month_start + timedelta(days=days_in_month - 1)
                    ts, te = month_ts_te_generator(phrase_month_start, phrase_month_end)

        # Day names handling like monday, tomorrow, etc
        else:
            # This is to indentify the duration between two days i.e., monday to friday.
            if dayname and len(dayname) > 1:
                d1 = " " + (' '.join(str(j) for j in dayname[0]))
                d2 = " " + (' '.join(str(k) for k in dayname[1]))

                phrase_time_1 = week_handler(d1, NOW)
                phrase_time_2 = week_handler(d2, NOW)

                ts, te = week_ts_te_generator(phrase_time_1, phrase_time_2)

            else:
                # This is to indentify the duration from some day till date.
                if dayname:
                    if till_found:
                        d1 = " " + (' '.join(str(j) for j in dayname[0]))
                        d2 = phrase.split("till")[1]

                        phrase_time_1 = week_handler(d1, NOW)
                        phrase_time_2 = r.parse(d2)[0]

                        if phrase_time_2 is None:
                            phrase_time_2 = NOW
                        else:
                            phrase_time_2 = week_handler(d2, NOW)

                        if phrase_time_2 is None:
                            phrase_time_2 = NOW
                        else:
                            phrase_time_2 = phrase_time_2

                        ts, te = week_ts_te_generator(phrase_time_1, phrase_time_2)
                    else:
                        phrase_time = week_handler(phrase, NOW)
                        ts, te = week_ts_te_generator(phrase_time, phrase_time)

                elif year_found or "year" in phrase:
                    ts = re.sub(r'-\d{2}-\d{2}\s(\d.+)', '-01-01T00:00:00', str(mphrase_time))
                    te = re.sub(r'-\d{2}-\d{2}\s(\d.+)', '-12-31T23:59:59', str(mphrase_time))

                # Specific single days
                else:
                    phrase_time = mphrase_time
                    ts, te = month_ts_te_generator(phrase_time, phrase_time)

        return ts, te


def month_ts_te_generator(ts, te):
    while ts > te:
        year_now = te.year + 1
        te = te.replace(year=year_now)
    else:
        timestart = ts.replace(hour=00, minute=00, second=0, microsecond=000).isoformat()
        timeend = te.replace(hour=23, minute=59, second=59, microsecond=000).isoformat()

    return timestart, timeend


def week_ts_te_generator(ts, te):
    while ts > te:
        week_now = te + timedelta(days=7)
        wn = week_now.day
        te = te.replace(day=wn)
    else:
        timestart = ts.replace(hour=00, minute=00, second=0, microsecond=000).isoformat()
        timeend = te.replace(hour=23, minute=59, second=59, microsecond=000).isoformat()

        return timestart, timeend


def year_handler(phrase, NOW):
    r = RecurringEvent(NOW)
    phrase_time = r.parse(phrase)[0]
    ammod_found = RE_AMMOD.search(phrase)

    if ammod_found:
        match = ammod_found.group('ammod')

        if match == " next" or match == " coming" or match == " upcoming":
            if " month" not in phrase:
                # Decreasing one year from phrase time to balance
                year_now = phrase_time.year - 1
                phrase_time = phrase_time.replace(year=year_now)
            else:
                pass

        elif match == " this":
            # Matching with Year of NOW
            year_now = NOW.year
            phrase_time = phrase_time.replace(year=year_now)

        elif match == " last" and " month" not in phrase:
            # Matching with Last year

            if phrase_time.year < NOW.year:
                phrase_time = phrase_time
            else:
                year_now = phrase_time.year - 1
                phrase_time = phrase_time.replace(year=year_now)
        else:
            phrase_time = phrase_time

    else:
        while phrase_time > NOW:
            year_now = phrase_time.year - 1
            phrase_time = phrase_time.replace(year=year_now)

        else:
            phrase_time = phrase_time

    return phrase_time


def week_handler(phrase, NOW):
    r = RecurringEvent(NOW)
    phrase_time = r.parse(phrase)[0]
    ammod_found = RE_AMMOD.search(phrase)

    if ammod_found:
        match = ammod_found.group('ammod')

        if match == " next" or match == " coming" or match == " upcoming":
            # checking next uncompleted day to match
            nxwknw = NOW + timedelta(days=8)
            if phrase_time > nxwknw:
                day_now = phrase_time + timedelta(days=-7)
                dn = day_now.day
                phrase_time = phrase_time.replace(day=dn)
            else:
                phrase_time = phrase_time

        elif match == " last":
            # Matching with Last year
            prwknw = NOW - timedelta(days=8)

            if phrase_time > prwknw:
                day_now = phrase_time - timedelta(days=7)
                dn = day_now.day
                phrase_time = phrase_time.replace(day=dn)
            else:
                phrase_time = phrase_time
        else:
            phrase_time = phrase_time

    else:
        while phrase_time > NOW:
            phrase_time = phrase_time - timedelta(days=7)

        else:
            phrase_time = phrase_time

    return phrase_time

