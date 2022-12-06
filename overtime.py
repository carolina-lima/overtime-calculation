from datetimerange import DateTimeRange
from datetime import datetime, timedelta

# day of the week as an integer, where Monday is 0 and Sunday is 6
extra = []
f = '%Y-%m-%d %H:%M:%S'
h ='%H:%M:%S'
start_scalation = "2022-06-28 15:00:00"
end_scalation = "2022-07-01 16:00:00"
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']

time_range = DateTimeRange(start_scalation, end_scalation)
print(f"A escala de plantão é: {time_range}")

for value in time_range.range(timedelta(days=1)):
    if value.weekday() == 5 or value.weekday() == 5:
        start = str(value.date()) + ' 00:00:00' 
        start_absolute = start if (
        datetime.strftime(value, f) != start_scalation
        ) else datetime.strftime(value, f)

        end = str(value.date()) + ' 23:59:59' 
        end_absolute = end_scalation if (
        value.date() == (datetime.strptime(end_scalation, f)).date()
        ) else end

        dif_jornada = (datetime.strptime(end_absolute, f) - datetime.strptime(start_absolute, f)).total_seconds()
        print(f"O plantão do dia {value.date()} ocorreu no sábado entre {start_absolute} e {end_absolute}.")
        
    else:
        inicio_jornada = datetime.strptime((str(value.date()) + ' 10:00:00'), f)
        fim_jornada = datetime.strptime((str(value.date()) + ' 19:00:00'), f)
        start = datetime.strptime((str(value.date()) + ' 00:00:00'), f) 
        end = datetime.strptime((str(value.date()) + ' 23:59:59'), f)         
        
        start_absolute = start if (
        datetime.strftime(value, f) != start_scalation
        ) else value

        end_absolute = datetime.strptime(end_scalation, f) if (
        value.date() == (datetime.strptime(end_scalation, f)).date()
        ) else end

        if inicio_jornada > start_absolute:
            extra.append(
                {'date': str(value.date()),
                'weekday': weekday[value.weekday()],
                'start':datetime.strftime(start_absolute, h) ,
                'end': datetime.strftime(inicio_jornada, h)}
                )

        if end_absolute > fim_jornada:
            extra.append(
                {'date': str(value.date()),
                'weekday': weekday[value.weekday()],
                'start':datetime.strftime(fim_jornada, h) ,
                'end': datetime.strftime(end_absolute, h)})

print(extra)
