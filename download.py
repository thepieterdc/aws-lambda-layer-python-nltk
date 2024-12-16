import nltk

DATASETS = {
    "punkt",
    "stopwords",
}

for dataset in DATASETS:
    nltk.download(dataset, download_dir='package/nltk_data')