import glob
from datetime import datetime
import os
import shutil
from get_page import check_start
from read_and_make_csv import start_reading
from localize_csv import _convert_to_local


def pre_read_check(source, name_now):
    if not source:
        check_start('{}{}'.format(name_now, '.html'), False)
    else:
        made_on = os.path.getctime(source)
        mod_tm = os.path.getmtime(source)
        print("last modified: ", mod_tm)
        print("created: ", made_on)
        print('now: ', datetime.timestamp(now))
        made_on_tOBJ = datetime.fromtimestamp(made_on)
        diff = now - made_on_tOBJ
        print('Seconds Since made:', diff.seconds)
        if diff.seconds >= 43200:
            print("Refreshing local Copy")
            os.makedirs("OLD COPIES", exist_ok=True)
            new = os.path.join("OLD COPIES", source)
            shutil.move(source, new)
            source = name_now + '.html'
            check_start(source, True)
            source = pre_read_check(name_now, name_now)
    return str(source)


file = glob.glob('./*.html')
now = datetime.now()
name_f = str(now).replace(' ', '~')
try:
    file = str(file[0])[2:]
    print('Working on: ', file)
except IndexError:
    if not file:
        check_start('{}{}'.format(name_f, '.html'), False)
        file = name_f + '.html'
checked_f = pre_read_check(file, name_f)
start_reading(checked_f)
out_pt = _convert_to_local('export.csv')
print(out_pt)
