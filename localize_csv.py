import csv
from datetime import datetime

import pytz
from tabulate import tabulate


def _convert_to_local(file):
    print('\n\n', '*' * 10)
    l = []
    f = open("export_local.csv", "w", encoding='utf8')
    f.write('MON,DAY,ID,HR,MN,NAME\n')
    with open(file, 'r') as sch:
        # inp = sch.read()
        source_time_zone = pytz.timezone("Asia/Tokyo")
        reader = csv.DictReader(sch)
        for row in reader:
            data = (row['MON'], row['DAY'], row['ID'], row['HR'], row['MN'], row['NAME'])  # MON,DAY,ID,HR,MN,NAME
            # f.write(str(data))
            source_mon = data[0]
            source_day = data[1]
            source_hour = data[3]
            source_min = data[4]
            source_time = datetime(2020, int(source_mon), int(source_day), int(source_hour), int(source_min), 00, 0000)
            source_date_with_timezone = source_time_zone.localize(source_time)
            # print(type(source_date_with_timezone))
            val = time_left(source_date_with_timezone)
            target_time_zone = pytz.timezone('Asia/Kolkata')
            writt = source_date_with_timezone.astimezone(target_time_zone)
            f.write('{},{},{},{}{}'.format(writt.strftime("%m,%d"), data[2],
                                           writt.strftime("%H,%M"), data[5], '\n'))
            # print(val,type(val))
            if val.days < 0:
                l.append([data[5], "Over"])
            else:
                l.append([data[5], val])

    table = tabulate(l, headers=['Name', 'Status'], tablefmt="plain")
    return table


def time_left(full_inp):
    now_ = datetime.now()
    target_time_zone = pytz.timezone('Asia/Kolkata')
    target_date_with_timezone = now_.astimezone(target_time_zone)
    left = full_inp - target_date_with_timezone
    return left


def write_names(file):
    with open(file, 'r') as sch:
        kek = open('names.txt', 'a')
        reader = csv.DictReader(sch)
        for row in reader:
            data = row['NAME']
            kek.write(str(data) + '\n')
        kek.close()

# write_names('export.csv')
