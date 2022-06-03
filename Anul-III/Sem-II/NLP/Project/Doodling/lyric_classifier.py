import csv
import time

import pandas as pd
from matplotlib import pyplot as plt
from num2words import num2words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from cleantext import clean
from models import build_models


def get_dataset(PATH, file_type='csv'):
    with open(PATH, encoding="utf8") as file:
        header, *lines = csv.reader(file)

    dict = {key: value for key, value in zip(header, list(map(list, zip(*lines))))}
    # print(dict[["artist_name"]])
    return dict, header


def bog(list_texts, preprocess_function, tokenize_function=None):
    start = time.time()
    cv = CountVectorizer(
        preprocessor=preprocess_function,
        # tokenizer=tokenize_function,
        max_features=1000,
        # ngram_range=(2, 2),  # construim un vocabular de bigrame
    )

    cv.fit(list_texts)
    features = cv.transform(list_texts)

    print(time.time() - start)
    return cv, features


def number_to_words(text):
    return ' '.join([num2words(word, lang="en") if word.isdigit() else word for word in text.split()])


def to_lower(text):
    return text.lower()


def preprocessing_1(text):
    return number_to_words(to_lower(clean(text)))


def personal_train_test_split(PATH):
    dict, categories = get_dataset(PATH)
    # print(categories)
    cv1, features1 = bog(dict["lyrics"], preprocessing_1)
    features1_array = features1.toarray()
    X_train, X_test, y_train, y_test = train_test_split(features1_array, dict["genre"], test_size=0.2, random_state=42)
    # print(len(list(set(dict["genre"]))))
    return X_train, X_test, y_train, y_test, categories, dict


def get_song_title(dict):
    return dict[2]


def write_in_file(models, dict, predicted_test):
    for model_index in range(len(models)):
        with open(OUTPUT_FOLDER_PATH + f'classification_{models[model_index]}.txt', 'w', encoding="utf-8") as f:
            f.write('id,label\n')
            if models[model_index] == "CNN":
                f.write('\n'.join(["{},{},{}".format(id, track_name, list(label).index(max(label)))
                                   for id, track_name, label in
                                   zip(dict[""], dict["track_name"], list(predicted_test[model_index]))]))
            else:
                f.write('\n'.join(["{},{},{}".format(id, track_name, label)
                                   for id, track_name, label in
                                   zip(dict[""], dict["track_name"], list(predicted_test[model_index]))]))


def save_stats(clf_train, predicted_validate, cms, crs, models):
    def save_cm(clf, cm, model):
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
        disp.plot()
        plt.title(f'{model} confusion matrix')
        # plt.show()
        plt.savefig(f'OUTPUT_FOLDER/{model}_confusion_matrix.png')
        plt.close()

    def save_cr(cr):
        if "accuracy" in cr.keys():
            cr.update({"accuracy": {"precision": None, "recall": None, "f1-score": cr["accuracy"], "support": cr['macro avg']['support']}})
        clsf_report = pd.DataFrame(cr).transpose()
        clsf_report.to_csv(f'OUTPUT_FOLDER/{model}.csv', index=True)
    for clf, predicted_valid, cm, cr, model in zip(clf_train, predicted_validate, cms, crs, models):
        save_cm(clf, cm, model)
        save_cr(cr)


if __name__ == "__main__":
    INPUT_FOLDER_PATH = "D:\\Facultate\\Anul III\\Sem II\\Introducere in prelucrarea limbajului natural " \
                        "NLP\\Project\\DataSets\\Music Dataset_ Lyrics and Metadata from 1950 to " \
                        "2019\\tcc_ceds_music.csv "
    X_train, X_test, y_train, y_test, categories, dict = personal_train_test_split(INPUT_FOLDER_PATH)
    # print(X_train[0])

    OUTPUT_FOLDER_PATH = "D:\\Facultate\\Anul III\\Sem II\\Introducere in prelucrarea limbajului natural " \
                         "NLP\\Project\\OUTPUT_FOLDER "
    models = ["DT", "SS_SGDClassifier", "RF", "SS_LinearSVC", "MLPC", "GNP", "SS_SVC_rbf"]
    # models = ["DT", "GNP", "RF"]

    clf_train, predicted_validate, predicted_test, cms, crs = build_models(X_train, y_train, X_test, models, X_test,
                                                                           y_test, DEBUG=True)
    save_stats(clf_train, predicted_validate, cms, crs, models)
    # write_in_file(models, dict, predicted_test)
