import csv
from get_pagerduty_scalation import list_pagerduty_scalation
from overtime import overtime_calculation, extra


escale = list_pagerduty_scalation()

for row in escale:
    overtime_calculation(row['start'],row['end'],row['user'],row['schedule_name'])

with open("overtime_escalation.csv", 'w') as file: 
            wr = csv.DictWriter(file, fieldnames = extra[0].keys()) 
            wr.writeheader() 
            for i in extra:
                wr.writerow(i)
