setup:
	pip install -r requirements.txt
chat:
	$(MAKE) delete-cache 
	adk web
venv:
	source .venv/bin/activate
delete-cache:
	find . -name "__pycache__" -type d -exec rm -rf {} +