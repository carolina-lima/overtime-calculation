import csv
from datetime import datetime


def list_pagerduty_scalation():
    escalation = []
    f = '%Y-%m-%d %H:%M:%S'
    with open('pagerduty_escalations_2022-07-01_2022-08-31 - pagerduty_escalations_2022-07-01_2022-08-31.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['start'] = datetime.strftime((datetime.fromisoformat(row['start'])),f)
            row['end'] = datetime.strftime((datetime.fromisoformat(row['end'])),f)
            escalation.append(row)
    return escalation
    