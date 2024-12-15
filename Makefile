download: prepare
	mkdir -p python/nltk_data
	python3 download.py

package: download
	zip -r layer.zip .

prepare:
	python3 -m pip install -r requirements.txt -t python