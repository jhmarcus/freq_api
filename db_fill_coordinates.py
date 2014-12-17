#!venv/bin/python
import time
import gzip
import sqlite3
import sys
from freq_api import db, models

t0 = time.time()

data_file = sys.argv[1]
dataset = sys.argv[2]

reader = open(data_file)

conn = sqlite3.connect('freq_api/static/app.db')
c = conn.cursor()

i = 1
for line in reader:
    fields = line.strip('\n').split()
    clst = fields[0]
    lon = fields[1]
    lat = fields[2]
    c.execute('INSERT INTO coordinates VALUES ("{}", "{}", {}, {})'.format(clst, dataset, lat, lon))

    if i%100000 == 0:
        print '{} rows parsed'.format(i)
    i+=1

conn.commit()
print str(time.time() - t0) + 'secs'
