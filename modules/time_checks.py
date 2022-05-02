from datetime import datetime, timezone, timedelta

DEFAULT_TIMEZONE = timezone(timedelta(hours=+3))
LATE_HOUR = 12
EVENING_HOUR = 17

def isTimeToRemind(events) -> bool: 
    if not events: return false
    
    now = datetime.now(DEFAULT_TIMEZONE)
    first_event_datetime = datetime.fromisoformat(events[0]['start'].get('dateTime', events[0]['start'].get('date')))
    
    if now > time_first_event: raise Exception("Events in past is not allowed")
        
    for event in events:
        event_datetime = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
        
        if event_datetime.date() != first_event_datetime.date():
            raise Exception("Events in different days is not allowed")
        
        if event_datetime < first_event_datetime:
            raise Exception("Events should be sorted")
    
    if first_event_datetime.date() > now.date() + timedelta(days = 1): 
        #Day after tomorrow no sense to remind
        return false
    
    if first_event_datetime.date() == now.date(): 
        #Today
        if now.hour < LATE_HOUR - 1:
            #Morning reminder
            return first_event_datetime.hour < EVENING_HOUR
        else:
            #Daytime reminder
            return true
    else:
        #Evening reminder for early tomorrow events
        return now.hour > LATE_HOUR and first_event_datetime.hour < LATE_HOUR
    
    raise Exception("Something wrong occured")

def getTimeBounds():
    begin = datetime.now(DEFAULT_TIMEZONE)

    if begin.hour > LATE_HOUR:
        #Too late to remind about today's events, so let's look for tomorrow
        begin += timedelta(days = 1)
        begin = begin.replace(hour=0, minute=0, second=0, microsecond=0)
    
    end = begin.replace(hour=23, minute=59, second=59, microsecond=0)

    return {
        'begin': begin, 
        'end': end    
    }

