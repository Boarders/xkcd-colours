code-dir = colours

default:
	python3 main.py

check:
	mypy $(code-dir)

format:
	black $(code-dir)
