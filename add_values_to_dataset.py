import csv
import datetime
from time import sleep
import random
FIELD_NAMES = ['date', 'value']


while True:
    sleep(300)
    with open('dataset-date-value.csv', 'a', newline='') as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=FIELD_NAMES)
        row = {'date': datetime.datetime.now(), 'value': random.randint(1, 1000)}
        dict_writer.writerow(row)
