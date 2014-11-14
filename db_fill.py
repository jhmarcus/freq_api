#!venv/bin/python
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from freq_api import db,models

t0 = time.time()

conn = db.engine.connect()
reader = open('freq_api/static/data/1000genomes.chr22.phase3.frq.strat.sample')
reader.readline()

i = 0
for line in reader:
    fields = line.strip('\n').split()
    if fields[1].count(':') == 1 or fields[1][:2] == 'rs':
        chr = fields[0]
        pos = fields[1].split(':')[1]
        snp = fields[1]
        clst = fields[2]
        a1 = fields[3]
        a2 = fields[4]
        maf = fields[5]
        mac = fields[6]
        nobs = fields[7]
        ins = models.Freq.__table__.insert().values(chr=chr, pos=pos, snp=snp, clst=clst, a1=a1, a2=a2, maf=maf, mac=mac, nobs=nobs)
        conn.execute(ins)
        if i%1000 == 0:
            print '{} variants added'.format(i)
        i+=1

print str(time.time() - t0) + 'secs'
