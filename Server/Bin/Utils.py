from urllib.request import urlopen
from json import load
import os


def get_localisation(addr: str=None) -> str:
    if addr is None or addr.startswith("192.168.") or addr.startswith("127.0"):
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    loc = ''
    for attr in data.keys():
        if attr == "city" or attr == "country" or attr == "region":
            loc += " " + str(data[attr]).replace('\u00f4', "o")
    return str(loc.removeprefix(" "))


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def clear_console():
    try:
        os.system("cls")
        os.system("clear")
    except:
        pass