download: prepare
	python3 download.py

package: download
	(cd package/; zip -r ../layer.zip .)

prepare:
	mkdir -p package/python/nltk_data
	python3 -m pip install -r requirements.txt
	python3 -m pip install -r requirements.txt -t package/python