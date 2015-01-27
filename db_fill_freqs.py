#!venv/bin/python
import time
import sqlite3
import sys
import gzip

t0 = time.time()

data_file = sys.argv[1]
dataset = sys.argv[2]

conn = sqlite3.connect('freq_api/static/app.db')
c = conn.cursor()

with gzip.open(data_file) as data:
    data.readline()
    i = 1
    for line in data:
        fields = line.strip('\n').split()
        if fields[1].count(':') == 1 or fields[1][:2] == 'rs':
            pos = fields[1]
            clst = fields[2]
            a1 = fields[3]
            a2 = fields[4]
            maf = fields[5]
            mac = fields[6]
            nobs = fields[7]
            c.execute('INSERT INTO freqs VALUES ("{}", {}, "{}", "{}", "{}", "{}", {}, {}, {})'.format(pos, i, clst, dataset,
                                                                                                       a1, a2, maf, mac, nobs))

            if i%100000 == 0:
                print '{} rows parsed'.format(i)
            i+=1

conn.commit()
print str(time.time() - t0) + 'secs'
