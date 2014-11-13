#!venv/bin/python
from freq_api import db, models

reader = open('freq_api/static/data/1000genomes.chr22.phase3.frq.strat')
reader.readline()

i = 0
for line in reader:
    fields = line.strip('\n').split()
    if fields[1].count(':') == 1 or fields[1][:2] == 'rs':
        f = models.Freq(chr=fields[0], pos=fields[1].split(':')[1], snp=fields[1], clst=fields[2],
                        a1=fields[3], a2=fields[4], maf=fields[5], mac=fields[6], nobs=fields[7])
        db.session.add(f)
        if i%100000 == 0:
            print '{} variants added'.format(i)
        i+=1

db.session.commit()
