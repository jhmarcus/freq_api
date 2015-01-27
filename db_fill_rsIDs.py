#!venv/bin/python
import time
import gzip
import sqlite3
import sys

t0 = time.time()

data_file = sys.argv[1]
build = sys.argv[2]

conn = sqlite3.connect('freq_api/static/app.db')
c = conn.cursor()

with gzip.open(data_file) as data:
    data.readline()
    i = 1
    for line in data:
        fields = line.strip('\n').split()
        snp = fields[0][3:]+':'+fields[2]
        rsID = fields[3]
        c.execute('INSERT INTO rsIDs VALUES ("{}", "{}", "{}")'.format(snp, rsID, build))

        if i%100000 == 0:
            print '{} rows parsed'.format(i)
        i+=1

conn.commit()
print str(time.time() - t0) + 'secs'
