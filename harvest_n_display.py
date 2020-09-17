import glob
from datetime import datetime
from get_page import make_file_html, pre_read_check
from read_and_make_csv import start_reading
from localize_csv import _convert_to_local


file_glob = glob.glob('./*.html')
now = datetime.now()
name_f = str(now).replace(' ', '~')
try:
    file_name = str(file_glob[0])[2:]
    print('Working on: ', file_name)
except IndexError:
    if not file_glob:
        file_name = name_f + '.html'
        make_file_html(file_name, False)

checked_f = pre_read_check(file_name, name_f, now)
start_reading(checked_f)
out_pt = _convert_to_local('export.csv')
print(out_pt)
