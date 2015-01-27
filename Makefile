create:
	./db_create.py
	./db_migrate.py

migrate:
	./db_migrate

clean:
	rm freq_api/*.pyc
	rm freq_api/static/app.db
	rm -rf freq_api/static/db_repository/  

sample:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr22.phase3.frq.strat.sample.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_22.bed.sample.gz GRCh37  
	./db_fill_coordinates.py freq_api/static/data/1000genomes/1000genomes_phase3_coordinates.txt 1000genomes_phase3

serve:
	python run.py

restart:
	sudo service apache2 reload
	sudo service apache2 restart

snp:
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&pos=22:16050069"

snp2:
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&pos=1:752566"

snp3: 
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&pos=22:16050607" 

snp4:
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&pos=22:27569979"

rsID:
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&rsID=rs1056"

rsID2:
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&rsID=rs587776127"

random:
	curl "http://127.0.0.1:5000/freq?dataset=1000genomes_phase3&random=True"

1000genomes: 1000genomes_chr1 1000genomes_chr2 1000genomes_chr3 1000genomes_chr4 1000genomes_chr5 1000genomes_chr6 1000genomes_chr7 1000genomes_chr8 1000genomes_chr9 1000genomes_chr10 1000genomes_chr11 1000genomes_chr12 1000genomes_chr13 1000genomes_chr14 1000genomes_chr15 1000genomes_chr16 1000genomes_chr17 1000genomes_chr18 1000genomes_chr19 1000genomes_chr20  1000genomes_chr21 1000genomes_chr22     
	./db_fill_coordinates.py freq_api/static/data/1000genomes/1000genomes_phase3_coordinates.txt 1000genomes_phase3

1000genomes_chr1:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr1.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_1.bed.gz GRCh37  

1000genomes_chr2:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr2.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_2.bed.gz GRCh37  

1000genomes_chr3:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr3.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_3.bed.gz GRCh37  

1000genomes_chr4:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr4.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_4.bed.gz GRCh37  

1000genomes_chr5:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr5.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_5.bed.gz GRCh37  

1000genomes_chr6:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr6.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_6.bed.gz GRCh37  

1000genomes_chr7:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr7.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_7.bed.gz GRCh37  

1000genomes_chr8:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr8.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_8.bed.gz GRCh37  

1000genomes_chr9:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr9.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_9.bed.gz GRCh37  

1000genomes_chr10:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr10.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_10.bed.gz GRCh37  

1000genomes_chr11:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr11.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_11.bed.gz GRCh37  

1000genomes_chr12:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr12.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_12.bed.gz GRCh37  

1000genomes_chr13:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr13.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_13.bed.gz GRCh37  

1000genomes_chr14:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr14.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_14.bed.gz GRCh37  

1000genomes_chr15:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr15.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_15.bed.gz GRCh37  

1000genomes_chr16:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr16.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_16.bed.gz GRCh37  

1000genomes_chr17:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr17.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_17.bed.gz GRCh37  

1000genomes_chr18:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr18.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_18.bed.gz GRCh37  

1000genomes_chr19:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr19.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_19.bed.gz GRCh37  

1000genomes_chr20:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr20.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_20.bed.gz GRCh37  

1000genomes_chr21:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr21.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_21.bed.gz GRCh37  

1000genomes_chr22:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr22.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_22.bed.gz GRCh37  

22:
	./db_fill_freqs.py freq_api/static/data/1000genomes/1000genomes.chr22.phase3.frq.strat.gz 1000genomes_phase3 
	./db_fill_rsIDs.py freq_api/static/data/rsIDs/GRCh37/bed_chr_22.bed.gz GRCh37  
	./db_fill_coordinates.py freq_api/static/data/1000genomes/1000genomes_phase3_coordinates.txt 1000genomes_phase3
