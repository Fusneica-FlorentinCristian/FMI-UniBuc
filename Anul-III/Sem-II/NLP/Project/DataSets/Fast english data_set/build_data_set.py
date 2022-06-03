import json
from time import time

import nltk
import numpy as np
import spacy
from nltk import SnowballStemmer
from num2words import num2words
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


def read_json():
    # Opening JSON file
    f = open('News_Category_Dataset_v2.json')

    # returns JSON object as a dictionary
    dataset = []

    x = f.readline()
    while x != '':
        dataset.append(json.loads(x))
        x = f.readline()

    # Closing file
    f.close()

    return dataset


#     return [dict(item, elem='value') for item in dataset]


def convert_limited(tup, tags):
    di = {}
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


def limited_categories(news, number_of_categories):
    news_clean = [(item["category"], item["headline"]) for item in news]

    categories = []
    for elem in news_clean:
        if elem[0] not in categories:
            categories.append(elem[0])
        if len(categories) == number_of_categories:
            break

    news_per_category = convert_limited(news_clean, categories)

    headlines = []
    for element in news_clean:
        if element[0] in categories:
            headlines.append(element[1])

    categories_classes = []
    for element in news_clean:
        if element[0] in categories:
            categories_classes.append(element[0])

    #     number_of_headlines = len(headlines)
    #     number_of_train = int(number_of_headlines*0.8)
    #     news_train = headlines[:number_of_train]
    #     news_test = headlines[number_of_train:]

    return news_clean, categories, news_per_category, headlines, np.array(categories_classes)


news = read_json()

NUMBER_OF_CATEGORIES = 1000
news_clean, categories, news_per_category, headlines, category_classes = limited_categories(news, NUMBER_OF_CATEGORIES)

print(len(categories))

nlp = spacy.load('en_core_web_sm')
stemmer = SnowballStemmer(language='english')
en_stop_words = nlp.Defaults.stop_words


def number_to_words(text):
    return ' '.join([num2words(word, lang="en") if word.isdigit() else word for word in text.split()])


def to_lower(text):
    return text.lower()


def tokenize(text):
    return list(nltk.word_tokenize(text))


def bog(list_texts, preprocess_function, tokenize_function):
    start = time()
    cv = CountVectorizer(
        preprocessor=preprocess_function,
        tokenizer=tokenize_function,
        token_pattern=None,
        max_features=100,
        ngram_range=(2, 2),  # construim un vocabular de bigrame
    )

    cv.fit(list_texts)
    features = cv.transform(list_texts)

    print(time() - start)
    return cv, features


def preprocessing1(text):
    return to_lower(number_to_words(text))


print("Before cv1")
cv1, features1 = bog(headlines, preprocessing1, tokenize)


def normalization(features, norma='l1'):
    scaler = preprocessing.Normalizer(norm=norma)

    scaler.fit(features)
    # scalam vectorii de train
    scaled_x = scaler.transform(features)

    return scaled_x


# POTI SA NORMALIZEZI FEATURE-URILE
# features1 = normalization(features1)

X_train, X_test, y_train, y_test = train_test_split(features1, category_classes, test_size=0.2, random_state=42)
