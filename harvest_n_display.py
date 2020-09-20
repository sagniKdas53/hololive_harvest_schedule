import glob
from datetime import datetime
from get_page import pre_read_check
from read_and_make_csv import start_reading
from localize_csv import _convert_to_local
from de_nihongfi import translate_export

'''Here i will write the functions that could and would be imported in the bot finally'''

file_glob = glob.glob('./*.html')
now = datetime.now()
name_f = str(now).replace(' ', '~')
file_name = ''
try:
    file_name = str(file_glob[0])[2:]
    print('Working on: ', file_name)
except IndexError:
    file_name = name_f + '.html'
    # make_file_html(file_name, False)

checked_f = pre_read_check(file_name, now)  # this returns the source html file
start_reading(checked_f)  # makes the export.csv (delocalized and untranslated)
translate_export('export.csv', 'names.txt', 'translate_names.txt')  # makes export_translated.csv
out_pt = _convert_to_local('export_translated.csv', 'Asia/Kolkata')  # takes in export_translated.csv and time zone
print(out_pt)  # table of names and status in input time zone.
