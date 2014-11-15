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

q:
	curl -H "Content-type: application/json" http://127.0.0.1:5000/api/freqs

qv:
	curl \
		-G \
		-H "Content-type: application/json" \
		-d "q={\"filters\":[{\"name\":\"snp\",\"op\":\"eq\",\"val\":\"22:45961213\"}]}" \
		http://127.0.0.1:5000/api/freqs

qv2:
	curl \
		-G \
		-H "Content-type: application/json" \
		-d "q={\"filters\":[{\"name\":\"rsID\",\"op\":\"eq\",\"val\":\"rs1118\"}]}" \
		http://127.0.0.1:5000/api/freqs
