import cv2
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.linear_model import SGDClassifier
import seaborn as sns


def read_file(file_name):
    # Opening JSON file
    try:
        print("Reading files:")
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
                    data_set["label"].append(data[1])
            elif header[0] == "id" and len(header) < 2:
                data_set["id"] = x[1:]
            else:
                raise Exception("File doesn't have the required format")

            return data_set
    except Exception as e:
        return e


def read_images(folder_path, filenames):
    start = time.time()
    arrays = []
    for filename in filenames:
        arrays.append(plt.imread(os.path.join(folder_path, filename)))
    print("Time for reading images in {}:".format(folder_path), time.time() - start)
    return np.array(arrays)


def normalize_images(images, axis=(1, 2)):
    mean = np.mean(images, axis=axis, keepdims=True)
    standard = np.sqrt(((images - mean) ** 2).mean(axis=axis, keepdims=True))
    new_array = (images - mean) / standard
    return new_array


def normalize_images_old(images):
    #     return cv2.normalize(img,  np.zeros((16,16)), 0, 255, cv2.NORM_MINMAX)
    return np.array(
        [cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F).flatten() for img in
         images])


def normalize_images_new(images):
    #     return cv2.normalize(img,  np.zeros((16,16)), 0, 255, cv2.NORM_MINMAX)
    return images / 255


def normalize_flatten_images(images):
    return normalize_images_old(images)


def classifier(X_train, y_train, model_number):
    start = time.time()
    match model_number:
        case 1:
            clf = make_pipeline(StandardScaler(), svm.SVC(kernel='rbf'))  # 0.55
        case 2:
            clf = make_pipeline(Normalizer(), svm.SVC(kernel='rbf'))  # 0.53
        case 3:
            clf = make_pipeline(StandardScaler(), SGDClassifier(random_state=42, max_iter=1000, tol=1e-3))  # 0,44
        case 4:
            clf = make_pipeline(StandardScaler(with_mean=False),
                                svm.LinearSVC(random_state=0, tol=1e-5, max_iter=10000))  # 0.47
        case _:
            clf = svm.SVC(kernel='rbf')  # 0.54

    clf.fit(X_train, y_train)
    print("Classification time: {}".format(time.time() - start))
    return clf


def metrics_data(classes, predicted_classes):
    return metrics.classification_report(classes, predicted_classes), metrics.confusion_matrix(classes, predicted_classes)


if __name__ == "__main__":
    FOLDER_PATH = "E:\Facultate\Anul II\Sem II\IA\ML\Kaggle\\"
    test_data = read_file(FOLDER_PATH + "test.txt")
    train_data = read_file(FOLDER_PATH + "train.txt")
    validation_data = read_file(FOLDER_PATH + "validation.txt")

    train_images = read_images(FOLDER_PATH + "train+validation", train_data["id"])
    test_images = read_images(FOLDER_PATH + "test", test_data["id"])
    validation_images = read_images(FOLDER_PATH + "train+validation", validation_data["id"])
    # print(len(train_images))

    train_images_normalized = normalize_images_old(train_images)
    validation_images_normalized = normalize_images_old(validation_images)
    test_images_normalized = normalize_images_old(test_images)

    X_train = train_images_normalized
    X_validate = validation_images_normalized
    X_test = test_images_normalized
    y_train = train_data["label"]
    y_validate = validation_data["label"]

    clf_train = []
    predicted_validate = []
    cm = []
    cr = []
    for model in range(2):
        clf_train.append(classifier(X_train, y_train, model))
        predicted_validate.append(clf_train[model].predict(X_validate))
        local_cr, local_cm = metrics_data(y_validate, predicted_validate[model])
        cr.append(local_cr)
        cm.append(local_cm)
        # print(cr[model])

    sns.heatmap(cm[1], annot=True, fmt='')
    plt.savefig(FOLDER_PATH + "heatmap.png")

    test_data["label"] = list(predicted_validate[1])
    with open(FOLDER_PATH + 'test_submission.txt', 'w') as f:
        f.write('id,label\n')
        f.write('\n'.join(
            ["{},{}".format(id_image, label) for id_image, label in zip(test_data["id"], test_data["label"])]))
