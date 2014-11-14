clean:
	rm freq_api/*.pyc
cleandb:
	rm app.db
	rm -rf db_repository/  
createdb:
	./db_create.py
	./db_migrate.py
