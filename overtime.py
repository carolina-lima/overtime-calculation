from datetimerange import DateTimeRange
from datetime import datetime, timedelta


extra = []
def overtime_calculation(start_scalation, end_scalation, user, schedule_name):
    
    f = '%Y-%m-%d %H:%M:%S'
    h ='%H:%M:%S'
    # day of the week as an integer, where Monday is 0 and Sunday is 6
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'thursday', 'Friday', 'Saturday', 'Sunday']

    s = datetime.strptime(start_scalation, f).date()
    e = datetime.strptime(end_scalation, f).date()

    time_range = DateTimeRange(s, e) #this helps timedelta iterate on dates that didn't complete exactly 1 day

    for value in time_range.range(timedelta(days=1)):
        if value.weekday() == 5 or value.weekday() == 6:
            start = datetime.strptime((str(value.date()) + ' 00:00:00'), f) 
            end = datetime.strptime((str(value.date()) + ' 23:59:59'), f)         
            
            start_absolute = start if (
            value.date() != s
            ) else datetime.strptime(start_scalation, f)

            end_absolute = datetime.strptime(end_scalation, f) if (
            value.date() == (datetime.strptime(end_scalation, f)).date()
            ) else end

            extra.append(
                {'name': user,
                'schedule': schedule_name,
                'date': str(value.date()),
                'weekday': weekday[value.weekday()],
                'start':datetime.strftime(start_absolute, h),
                'end': datetime.strftime(end_absolute, h)}
                )

        else:
            inicio_jornada = datetime.strptime((str(value.date()) + ' 10:00:00'), f)
            fim_jornada = datetime.strptime((str(value.date()) + ' 19:00:00'), f)
            start = datetime.strptime((str(value.date()) + ' 00:00:00'), f) 
            end = datetime.strptime((str(value.date()) + ' 23:59:59'), f)         
            
            start_absolute = start if (
            value.date() != s
            ) else datetime.strptime(start_scalation, f)

            end_absolute = datetime.strptime(end_scalation, f) if (
            value.date() == (datetime.strptime(end_scalation, f)).date()
            ) else end

            if inicio_jornada > start_absolute:
                extra.append(
                    {'name': user,
                    'schedule': schedule_name,
                    'date': str(value.date()),
                    'weekday': weekday[value.weekday()],
                    'start':datetime.strftime(start_absolute, h) ,
                    'end': datetime.strftime(inicio_jornada, h)}
                    )

            if end_absolute > fim_jornada:
                extra.append(
                    {'name': user,
                    'schedule': schedule_name,
                    'date': str(value.date()),
                    'weekday': weekday[value.weekday()],
                    'start':datetime.strftime(fim_jornada, h) ,
                    'end': datetime.strftime(end_absolute, h)})
    return extra
