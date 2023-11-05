fl:
	flask --app .\api\main.py run --debug

g-headers:
	py .\api\browserHeaders.py

test-all:
	py .\api\test\test-generate.py
