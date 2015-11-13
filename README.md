freq_api
========

A REST API for geographically distributed allele frequency data.  This serves as the backend for the GGV browser (http://popgen.uchicago.edu/ggv) and is part of a BD2K Targeted Software Development project.

The API was built using ...

* Flask-RESTful 
* Flask-SQLAlchemy  
* sqlite

## Example calls

Example to pull SNP frequencies per population from 1000 genomes using chr / pos:
(http://popgen.uchicago.edu/ggv_api/freq_table?data=%221000genomes_phase3_table%22&chr=1&pos=3072692)

Using rsid:
(http://popgen.uchicago.edu/ggv_api/freq_table?data=%221000genomes_phase3_table%22&rsID=rs12632844)

A random SNP:
(http://popgen.uchicago.edu/ggv_api/freq_table?data=%221000genomes_phase3_table%22&random_snp=True)


## Data  
* 1000 Genomes
* HGDP 
* POPRES 
* [hg18 rsIDs](http://hgdownload.cse.ucsc.edu/goldenPath/hg18/database/snp130.txt.gz)
* [hg19 rsIDs](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/snp141.txt.gz)

## References 

* [Very Helpful Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
* [Very Helpful Tutorial II](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
