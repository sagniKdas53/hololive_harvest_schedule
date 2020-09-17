import wget
import os
import shutil
from datetime import datetime


def is_file(url, file):
    my_url = url

    r = file
    if not os.path.isfile(r):
        wget.download(my_url, r)


def make_file_html(file, force):
    r = file
    url = "https://schedule.hololive.tv/"
    if not os.path.isfile(r):
        is_file(url, r)
    if force:
        is_file(url, r)


def pre_read_check(source, time_o):
    made_on = os.path.getctime(source)
    mod_tm = os.path.getmtime(source)
    print("last modified: ", mod_tm)
    print("created: ", made_on)
    print('now: ', datetime.timestamp(time_o))
    made_on_tOBJ = datetime.fromtimestamp(made_on)
    diff = time_o - made_on_tOBJ
    print('Seconds Since made:', diff.seconds)
    if int(diff.seconds) >= 43200:
        print("Refreshing local Copy")
        now = datetime.now()
        name_now = str(now).replace(' ', '~')
        os.makedirs("OLD COPIES", exist_ok=True)
        move_location = os.path.join("OLD COPIES", source)
        shutil.move(source, move_location)
        source = name_now + '.html'
        make_file_html(source, True)
        refreshed_f = pre_read_check(name_now, now)
        return str(refreshed_f)
    else:
        return str(source)
