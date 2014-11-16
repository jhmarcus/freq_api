#!venv/bin/python
import time
import gzip
import sqlite3
import sys
from freq_api import db,models

t0 = time.time()

data_file = sys.argv[1]
build = sys.argv[2]

reader = gzip.open(data_file)
reader.readline()

conn = sqlite3.connect('app.db')
c = conn.cursor()

i = 1
for line in reader:
    fields = line.strip('\n').split()
    snp = fields[0][3:]+':'+fields[2]
    rsID = fields[3]
    c.execute('INSERT INTO rsIDs VALUES ("{}", "{}", "{}")'.format(snp, rsID, build))

    if i%100000 == 0:
        print '{} rows parsed'.format(i)
    i+=1

conn.commit()
print str(time.time() - t0) + 'secs'
