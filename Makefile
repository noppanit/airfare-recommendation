test:
	py.test tests/*.py

create_graph:
	python scripts/import_data.py

delete_all:
	python scripts/delete_all.py
