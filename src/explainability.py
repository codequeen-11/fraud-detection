import shap 
import matplotlib.pyplot as plt
import pandas as pd


def get_feature_importance(model, feature_names):

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance_df = (
        importance_df
        .sort_values(
            "Importance",
            ascending=False
        )
    )

    return importance_df


def plot_top_features(
    importance_df,
    top_n=10
):

    plt.figure(figsize=(10, 6))

    importance_df.head(top_n).plot(
        kind="barh",
        x="Feature",
        y="Importance",
        legend=False
    )

    plt.title(
        f"Top {top_n} Feature Importances"
    )

    plt.gca().invert_yaxis()

    plt.show()