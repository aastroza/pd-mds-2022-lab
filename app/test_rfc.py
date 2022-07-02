import pandas as pd
from main import rfc
from sklearn.metrics import f1_score

def test_accuracy():

    # Load test data
    taxi_test = pd.read_csv('./data/yellow_tripdata_2020-03_test.csv')

    numeric_feat = [
    "pickup_weekday",
    "pickup_hour",
    'work_hours',
    "pickup_minute",
    "passenger_count",
    'trip_distance',
    'trip_time',
    'trip_speed'
    ]
    categorical_feat = [
        "PULocationID",
        "DOLocationID",
        "RatecodeID",
    ]

    features = numeric_feat + categorical_feat
    target_col = "high_tip"

    # Predict test examples
    preds_test = rfc.predict_proba(taxi_test[features])
    preds_test_labels = [p[1] for p in preds_test.round()]

    # Compute f1-score of classifier
    f1 = f1_score(taxi_test[target_col], preds_test_labels)


    # f1-score should be over 0.7
    assert f1 > 0.7