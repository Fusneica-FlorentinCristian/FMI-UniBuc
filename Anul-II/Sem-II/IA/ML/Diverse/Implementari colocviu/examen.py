import cv2
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
from tensorflow import keras
from keras import Input, activations
from keras.callbacks import EarlyStopping
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.losses import CategoricalCrossentropy
from keras.models import Sequential
from sklearn import svm, metrics, tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import NearestNeighbors, KNeighborsRegressor
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.linear_model import SGDClassifier, Ridge, RidgeCV, LinearRegression, Perceptron
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier


NUMBER_OF_LABELS = 7
WIDTH_IMAGE = 16
HEIGHT_IMAGE = 16
CHANNELS = 3

NUME = "FUSNEICA"
PRENUME = "FLORENTIN-CRISTIAN"
GRUPA = "341"


def read_file(file_name):
    # Opening JSON file
    try:
        print(f"Reading files from {file_name}.")
        with open(file_name, "r") as f:
            x = [line.strip() for line in f.readlines()]
            #             print(x)
            header = x[0].split(',')
            data_set = {
                "id": [],
                "label": []
            }
            if len(header) == 2 and header[0] == "id" and header[1] == "label":
                for line in range(1, len(x)):
                    data = x[line].split(",")
                    data_set["id"].append(data[0])
                    data_set["label"].append(int(data[1]))
            elif header[0] == "id" and len(header) < 2:
                data_set["id"] = x[1:]
            else:
                raise Exception("File doesn't have the required format")

            return data_set
    except Exception as e:
        return e


# def read_images(folder_path, filenames):
#     start = time.time()
#     arrays = []
#     for filename in filenames:
#         arrays.append(plt.imread(os.path.join(folder_path, filename)))
#     print("Time for reading images in {}:".format(folder_path), time.time() - start)
#     return arrays


def classifier(X, y, X_validate, y_validate, model, model_type=0):
    start = time.time()
    match model:
        case "SS_SVC_rbf":
            clf = make_pipeline(StandardScaler(), svm.SVC(kernel='rbf'))  # 0.55
        case "N_SVC_rbf":
            clf = make_pipeline(Normalizer(), svm.SVC(kernel='rbf'))  # 0.53
        case "SS_SGDClassifier":
            clf = make_pipeline(StandardScaler(), SGDClassifier(random_state=42, max_iter=1000, tol=1e-3))  # 0,44
        case "SS_LinearSVC":
            clf = make_pipeline(StandardScaler(with_mean=False),
                                svm.LinearSVC(random_state=0, tol=1e-5, max_iter=1000))  # 0.47
        case "SVC_rbf":
            clf = svm.SVC(kernel='rbf')  # 0.54
        case "RidgeCV":
            clf = RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1])
        case "Ridge":
            clf = Ridge(alpha=1.0)
        case "DT":
            clf = DecisionTreeClassifier(random_state=0, max_depth=2)
        case "DTR":
            clf = tree.DecisionTreeRegressor()
        case "KNN":
            clf = NearestNeighbors(n_neighbors=1)
            model_type = 1
        case "KNNRegressor":
            clf = KNeighborsRegressor(n_neighbors=2)
        case "LRegressor":
            clf = LinearRegression()
        case "MLPC":
            clf = MLPClassifier(random_state=1, max_iter=300)
        case "MLPRegressor":
            clf = MLPRegressor(random_state=1, max_iter=500)
        case "GNP":
            clf = GaussianNB()
        case "RF":
            clf = RandomForestClassifier(max_depth=2, random_state=0)
        case "Perceptron":
            clf = Perceptron(tol=1e-3, random_state=0)
        case "CNN":
            model_type = 3
            clf = get_encoder_model()
        case _:
            clf = svm.SVC(kernel='rbf')  # 0.54

    if model_type == 0:
        clf.fit(X, y)
    elif model_type == 1:
        clf.fit(X)
    elif model_type == 3:
        batch_size = 32
        epochs = 50
        early_stopping = EarlyStopping(monitor='val_loss', patience=3, min_delta=0.003)
        # clf.fit(x=X, y=to_keras_labels(y), validation_data=(X_validation, to_keras_labels(y_validation)), epochs=epochs, batch_size=batch_size, callbacks=[early_stopping])
        # clf.fit(x=X, y=np.array(y, dtype='float32'), validation_data=(X_validation, np.array(y_validation, dtype='float32')), epochs=epochs, batch_size=batch_size, callbacks=[early_stopping])
        metrics_clf = clf.fit(x=X, y=to_keras_labels(y),  validation_data=(X_validate, to_keras_labels(y_validate)), epochs=epochs, batch_size=batch_size, callbacks=[early_stopping])
    print(f"Classification time for {model}: {time.time() - start}")
    return clf


def to_keras_labels(labels):
    return to_categorical(labels, num_classes=NUMBER_OF_LABELS).tolist()


def get_encoder_model(DROPOUT_RATE=0.003, no_of_labels=NUMBER_OF_LABELS, width=WIDTH_IMAGE, height=HEIGHT_IMAGE, channels=CHANNELS):
    #  no_of_labels is the number of labels you want to train the NN (in Kaggle example, we had 7 labels)
    #  DROPOUT_RATE is the moment it drops if the model doesn't improve by this value (?)
    #  width and height are the size of the data (if it is 16x16, the width will be 16)
    #  channels are the 3rd dimension of the data, like in images with colours, rgb have 3 channels of colour

    encoder = Sequential([
        # RandomFlip("horizontal"),
        # RandomRotation(0.1),
        Input(shape=(width, height, channels)),

        Conv2D(filters=width, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        Conv2D(filters=width, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        MaxPooling2D(pool_size=(2, 2), strides=2),
        Dropout(rate=DROPOUT_RATE),

        # Conv2D(filters=WIDTH * 2, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        Conv2D(filters=width * 2, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        Conv2D(filters=width * 2, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        MaxPooling2D(pool_size=(2, 2), strides=2),
        Dropout(rate=DROPOUT_RATE),

        # Conv2D(filters=WIDTH * 4, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        Conv2D(filters=width * 4, kernel_size=(3, 3), activation=activations.relu, padding="same"),
        MaxPooling2D(pool_size=(2, 2), strides=2),
        # LayerNormalization(),

        Dropout(rate=DROPOUT_RATE),
        Flatten(),

        Dense(units=width * 4, activation=activations.relu),
        Dropout(rate=DROPOUT_RATE * 1.2),
        Dense(units=no_of_labels, activation=activations.softmax)
    ])

    # scheduler = LearningRateScheduler(scheduler)
    encoder.compile(loss=CategoricalCrossentropy(), optimizer=keras.optimizers.Adam(0.003),  # 0.0001
                    metrics=['accuracy'], run_eagerly=False)

    return encoder


def metrics_data(classes, predicted_classes):
    return metrics.classification_report(classes, predicted_classes), metrics.confusion_matrix(classes,
                                                                                               predicted_classes)


def build_models(X_train, y_train, X_validate, y_validate, X_test, models):
    clf_train, predicted_validate, predicted_test, cm_validate, cr_validate = [[] for _ in range(5)]
    for model_index in range(len(models)):
        if models[model_index] != "CNN":
            X_train = [np.array(elem).flatten().tolist() for elem in X_train]
            X_validate = [np.array(elem).flatten().tolist() for elem in X_validate]
            X_test = [np.array(elem).flatten().tolist() for elem in X_test]
        clf_train.append(classifier(X_train, y_train, X_validate, y_validate, models[model_index]))

        if isinstance(clf_train[model_index], Sequential):
            # predicted.append(clf_train[model_index].predict(to_keras_labels(X_validate)))
            # predicted_validate.append(clf_train[model_index].predict(X_validate))
            predicted_test.append(clf_train[model_index].predict(X_test))
            predicted_validate.append([])
            cr_validate.append([])
            cm_validate.append([])
        else:
            predicted_validate.append(clf_train[model_index].predict(X_validate))
            predicted_test.append(clf_train[model_index].predict(X_test))
            local_cr, local_cm = metrics_data(y_validate, predicted_validate[model_index])
            cr_validate.append(local_cr)
            cm_validate.append(local_cm)

    return clf_train, predicted_validate, predicted_test, cm_validate, cr_validate


def elements_in_list(my_list):
    return [[float(thing) for thing in elem.flatten()] for elem in my_list]


if __name__ == "__main__":
    INPUT_FOLDER_PATH = "D:\Facultate\Anul II\Sem II\IA\ML\Implementari colocviu\Colocviu 2021\\"
    OUTPUT_FOLDER_PATH = "D:\Facultate\Anul II\Sem II\IA\ML\Implementari colocviu\predictions\\"
    test_data = read_file(INPUT_FOLDER_PATH + "test_data.npy")
    train_data = read_file(INPUT_FOLDER_PATH + "train_data.npy")
    validation_data = read_file(INPUT_FOLDER_PATH + "train_labels.npy")

    train_images = read_images(INPUT_FOLDER_PATH + "train+validation", train_data["id"])
    test_images = read_images(INPUT_FOLDER_PATH + "test", test_data["id"])
    validation_images = read_images(INPUT_FOLDER_PATH + "train+validation", validation_data["id"])

    # X_train = elements_in_list(train_images)
    # X_validate = elements_in_list(validation_images)
    # X_test = elements_in_list(test_images)
    X_train = [elem.tolist() for elem in train_images]
    X_validate = [elem.tolist() for elem in validation_images]
    X_test = [elem.tolist() for elem in test_images]
    y_train = train_data["label"]
    y_validate = validation_data["label"]

    models = ["CNN", "SS_SVC_rbf", "Perceptron"]  # , "N_SVC_rbf", "SS_SGDClassifier", "SVC_rbf"]
    clf_train, predicted_validate, predicted_test, cm, cr = build_models(X_train, y_train, X_validate, y_validate, X_test, models)
    print("CONGRATS")
    for model_index in range(len(models)):
        with open(OUTPUT_FOLDER_PATH + f'classification_{models[model_index]}.txt', 'w') as f:
            f.write('id,label\n')
            if models[model_index] == "CNN":
                f.write('\n'.join(["{},{}".format(id_image, list(label).index(max(label)))
                                   for id_image, label in zip(test_data["id"], list(predicted_test[model_index]))]))
            else:
                f.write('\n'.join(["{},{}".format(id_image, label)
                               for id_image, label in zip(test_data["id"], list(predicted_test[model_index]))]))