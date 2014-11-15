#!venv/bin/python
import time
import gzip
import sqlite3
from freq_api import db,models

t0 = time.time()

reader = gzip.open('freq_api/static/data/rsIDs/GRCh37/bed_chr_22.bed.gz')
reader.readline()

conn = sqlite3.connect('app.db')
c = conn.cursor()

i = 1
for line in reader:
    fields = line.strip('\n').split()
    chr_pos = fields[0][3:]+':'+fields[2]
    rsID = fields[3]
    c.execute('INSERT INTO rsIDs VALUES ("{}", "{}")'.format(chr_pos, rsID))

    if i%100000 == 0:
        print '{} rows parsed'.format(i)
    i+=1

conn.commit()
print str(time.time() - t0) + 'secs'
