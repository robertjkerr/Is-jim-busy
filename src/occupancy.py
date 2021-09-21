##
## Python functions for finding and logging the occupancy of the St Andrews Uni gym
##

from bs4 import BeautifulSoup as _bs
import requests as _req
import csv as _csv
from datetime import datetime as _datetime

def __get_soup():
    source = _req.get("https://www.st-andrews.ac.uk/sport/").text
    soup = _bs(source, 'lxml')
    return soup

def get_occupancy():
    soup = __get_soup()
    tags = soup.find_all('h3')

    is_occup = lambda tag: "Occupancy:" in tag.text
    occup_tag = str(tuple(filter(is_occup, tags))[0])

    perc_index = occup_tag.index("%")
    occupancy = occup_tag[perc_index - 2: perc_index]
    return int(occupancy)

def write_log(occupancy, filename):
    now = _datetime.now()
    current_time = now.strftime("%H:%M:%S")
    fields = {"Occupancy": occupancy, "Time": current_time}

    with open(filename, 'a+') as file:
        writer = _csv.DictWriter(file, fields.keys())
        writer.writerow(fields)
        
