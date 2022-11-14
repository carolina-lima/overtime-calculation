from datetimerange import DateTimeRange
from datetime import datetime, timedelta

# day of the week as an integer, where Monday is 0 and Sunday is 6
extra = []
f = '%Y-%m-%d %H:%M:%S'
start_scalation = "2022-06-28 15:00:00"
end_scalation = "2022-07-01 16:00:00"

time_range = DateTimeRange(start_scalation, end_scalation)
print(f"A escala de plantão é: {time_range}")

for value in time_range.range(timedelta(days=1)):
    if value.weekday() == 5:
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

    elif value.weekday() == 6:
        start = str(value.date()) + ' 00:00:00' 
        start_absolute = start if (
        datetime.strftime(value, f) != start_scalation
        ) else datetime.strftime(value, f)

        end = str(value.date()) + ' 23:59:59' 
        end_absolute = end_scalation if (
        value.date() == (datetime.strptime(end_scalation, f)).date()
        ) else end

        dif_jornada = (datetime.strptime(end_absolute, f) - datetime.strptime(start_absolute, f)).total_seconds()
        print(f"O plantão do dia {value.date()} ocorreu no domingo entre {start_absolute} e {end_absolute}.")
        
    else:
        inicio_jornada = str(value.date()) + ' 10:00:00'
        fim_jornada = str(value.date()) + ' 19:00:00'

        start = str(value.date()) + ' 00:00:00' 
        start_absolute = start if (
        datetime.strftime(value, f) != start_scalation
        ) else datetime.strftime(value, f)

        end = str(value.date()) + ' 23:59:59' 
        end_absolute = end_scalation if (
        value.date() == (datetime.strptime(end_scalation, f)).date()
        ) else end

        print(f"No dia {value.date()} colaborador começou o plantão em {start_absolute}") 
        print(f"e parou de trabalhar em {end_absolute}")

        dif_antes_jornada = 0 if (
            datetime.strptime(inicio_jornada, f) < datetime.strptime(start_absolute, f)
            ) else (
            datetime.strptime(inicio_jornada, f) - datetime.strptime(start_absolute, f)
            ).total_seconds()

        dif_depois_jornada = 0 if (
            datetime.strptime(end_absolute, f) < datetime.strptime(fim_jornada, f)
            ) else (
            datetime.strptime(end_absolute, f) - datetime.strptime(fim_jornada, f)
            ).total_seconds()

        extra_seconds = dif_antes_jornada + dif_depois_jornada
        extra_hours = str(timedelta(seconds = extra_seconds))

        extra.append({'date': str(value.date()), 'extra_hours':extra_hours })

print(extra)