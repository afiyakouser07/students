from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def train_model(df):

    model_df = df.copy()

    le = LabelEncoder()

    model_df["placement_status"] = le.fit_transform(
        model_df["placement_status"]
    )

    X = model_df.drop("placement_status", axis=1)
    y = model_df["placement_status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy, X.columns
