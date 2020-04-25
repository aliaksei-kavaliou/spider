PYTHON = $(shell which python3)

run: 
	$(PYTHON) bug.py

test:
	$(PYTHON) -m unittest