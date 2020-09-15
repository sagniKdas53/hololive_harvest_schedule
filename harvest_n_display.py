import csv
import glob
import os
import re
import shutil
from datetime import datetime

import pytz
import wget
from bs4 import BeautifulSoup as _soup_


def is_file(url, file):
    my_url = url

    r = file
    if not os.path.isfile(r):
        wget.download(my_url, r)


def check_start(file, force):
    r = file
    url = "https://schedule.hololive.tv/"
    if not os.path.isfile(r):
        is_file(url, r)
    if force:
        is_file(url, r)


def start_reading(file):
    dayl = []
    hold = [0, 0]
    ms = 0
    f = open(file)  # simplified for the example (no urllib)
    flip_soup = _soup_(f, "html.parser")
    f.close()
    containers_date = flip_soup.find_all('div', class_="holodule navbar-text")
    containers_link = flip_soup.find_all('a', class_="thumbnail")
    for dates in containers_date:
        day = dates.text.strip().replace(' ', '').split()
        dayl.append(day[0].split('/'))
    print(dayl)
    f = open("export.csv", "w", encoding='utf8')
    f.write('MON,DAY,ID,HR,MN,NAME\n')
    for k in range(0, len(containers_link)):
        match = re.findall(r'href="https:[//]*www\.youtube\.com/watch\?v=([0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*)',
                           str(containers_link[k]))[0]
        time_name = containers_link[k].text.replace(' ', '').split()
        hr = time_name[0].split(':')
        if int(hr[0]) != 23 and int(hr[1]) <= 59 and hold[0] == 23:
            ms += 1
            f.write('{},{},{},{},{},{}{}'.format(dayl[ms][0], dayl[ms][1],
                                                 match,
                                                 hr[0], hr[1], time_name[1], '\n'))
            hold = [int(hr[0]), int(hr[1])]
        else:
            f.write('{},{},{},{},{},{}{}'.format(dayl[ms][0], dayl[ms][1],
                                                 match,
                                                 hr[0], hr[1], time_name[1], '\n'))
            hold = [int(hr[0]), int(hr[1])]
    f.close()


def time_left(full_inp):
    noxw = datetime.now()
    target_time_zone = pytz.timezone('Asia/Kolkata')
    target_date_with_timezone = noxw.astimezone(target_time_zone)
    left = full_inp - target_date_with_timezone
    return left, target_date_with_timezone


def _convert_to_local(file):
    print('\n\n', '*' * 10)
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
            # print(val, type(val))
            if val[0].days < 0:
                print(data[5], ':', "Over")
            else:
                print(data[5], ':', val[0].seconds)
            f.write('{},{},{},{}{}'.format(val[1].strftime("%m,%d"), data[2],
                                           val[1].strftime("%H,%M"), data[5], '\n'))


def main():
    file = glob.glob('./*.html')
    now = datetime.now()
    name_f = str(now).replace(' ', '~')
    # print(str(file[0]), name_f)
    try:
        file = str(file[0])[2:]
        print(file)
    except IndexError:
        if not file:
            check_start('{}{}'.format(name_f, '.html'), False)
    else:
        made_on = os.path.getctime(file)
        mod_tm = os.path.getmtime(file)
        print("last modified: ", mod_tm)
        print("created: ", made_on)
        print('now: ', datetime.timestamp(now))
        made_on_tOBJ = datetime.fromtimestamp(made_on)
        diff = now - made_on_tOBJ
        print('Seconds Since made:', diff.seconds)
        if diff.seconds >= 43200:
            os.makedirs("OLD COPIES", exist_ok=True)
            new = os.path.join("OLD COPIES", file)
            shutil.move(file, new)
            check_start('{}{}'.format(name_f, '.html'), True)
            main()
    start_reading(str(file))
    _convert_to_local('export.csv')


main()
