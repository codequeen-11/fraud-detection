from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    average_precision_score,
    f1_score
)

import pandas as pd


def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]

    results = {
        "AUC_PR": average_precision_score(
            y_test,
            y_prob
        ),
        "F1_Score": f1_score(
            y_test,
            y_pred
        )
    }

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    return results, cm