import numpy as np
from sklearn.metrics import classification_report, confusion_matrix


def mean_absolute_percentage_error(y_true, y_predictions):
    """
    :param y_true:
    :param y_predictions:
    :return:
    """
    error_sum = np.abs(np.array(y_true) - np.array(y_predictions)) * 100 / np.array(y_true)
    return round(np.mean(error_sum)[0], 2)


def print_classification_results(y_true, y_predictions):
    """
    :param y_true:
    :param y_predictions:
    :return:
    """
    print(f"Confusion Matrix\n{confusion_matrix(y_true, y_predictions)}\nClassification Report\n"
          f"{classification_report(y_true, y_predictions)}")
