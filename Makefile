clean:
	rm freq_api/*.pyc
cleandb:
	rm app.db
	rm -rf db_repository/  
createdb:
	./db_create.py
	./db_migrate.py
	./db_fill_freqs.py
	./db_fill_rsIDs.py

qpos:
	curl "http://127.0.0.1:5000/freq?chr=22&pos=16050069"

qrsID:
	curl "http://127.0.0.1:5000/freq?rsID=rs1118"
