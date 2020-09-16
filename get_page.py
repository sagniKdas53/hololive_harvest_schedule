import wget
import os


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
