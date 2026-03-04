def allocate_platform(train_data, total_platforms=5):
    platform_usage = {i: 0 for i in range(1, total_platforms + 1)}

    for _, row in train_data.iterrows():
        least_used = min(platform_usage, key=platform_usage.get)
        platform_usage[least_used] += row["passenger_load"]

    return platform_usage


def congestion_score(train_data):
    total_passengers = train_data["passenger_load"].sum()
    peak_trains = train_data[train_data["arrival_hour"].between(8, 11)].shape[0]

    score = (total_passengers / 1000) + (peak_trains * 2)
    return round(score, 2)