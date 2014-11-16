clean:
	rm freq_api/*.pyc

cleandb:
	rm freq_api/static/app.db
	rm -rf freq_api/static/db_repository/  

createdb:
	./db_create.py
	./db_migrate.py
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr22.phase3.frq.strat 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_22.bed.gz GRCh37  

restart:
	sudo service apache2 reload
	sudo service apache2 restart

qsnp:
	curl "http://127.0.0.1:5000/freq?chr=22&pos=16050069"

qrsID:
	curl "http://127.0.0.1:5000/freq?rsID=rs1118"
