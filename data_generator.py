import pandas as pd
import numpy as np

def generate_synthetic_data(n=1000):
    np.random.seed(42)

    train_ids = [f"TR{1000+i}" for i in range(n)]
    stations = ["Hyderabad", "Secunderabad", "Warangal", "Vijayawada", "Kazipet"]

    data = pd.DataFrame({
        "train_id": train_ids,
        "station": np.random.choice(stations, n),
        "arrival_hour": np.random.randint(0, 24, n),
        "scheduled_platform": np.random.randint(1, 6, n),
        "passenger_load": np.random.randint(100, 1500, n),
        "track_available": np.random.choice([0, 1], n, p=[0.2, 0.8]),
        "weather_score": np.random.randint(1, 5, n)
    })

    data["delay_minutes"] = (
        (data["passenger_load"] / 100) +
        (5 * (1 - data["track_available"])) +
        (3 * data["weather_score"]) +
        np.random.normal(0, 5, n)
    ).astype(int)

    data["delay_minutes"] = data["delay_minutes"].apply(lambda x: max(x, 0))

    return data