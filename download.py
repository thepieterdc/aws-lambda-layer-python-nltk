import nltk

DATASETS = {
    "averaged_perceptron_tagger",
    "brown",
    "conll2000",
    "movie_reviews",
    "punkt",
    "wordnet",
}

for dataset in DATASETS:
    nltk.download(dataset, download_dir='python/nltk_data')