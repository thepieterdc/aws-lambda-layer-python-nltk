import nltk

DATASETS = {
    "punkt_tab",
    "stopwords",
}

for dataset in DATASETS:
    nltk.download(dataset, download_dir='package/nltk_data')