# SmartRail Planner
AI-Based Railway Resource Allocation & Delay Optimization System

## Problem Statement
Railway systems handle multiple trains, tracks, platforms, and schedules daily.
Manual allocation often leads to inefficient resource usage and delays.
This project builds a smart AI-driven planner to optimize platform allocation and predict delays using synthetic railway data.

## Features

- Synthetic dataset generation (realistic simulation)
- Delay prediction using Random Forest Regression
- Intelligent platform allocation
- Congestion scoring system
- Interactive Streamlit dashboard
- Fully self-contained (no external railway data used)

## Approach

1. Generated realistic synthetic railway dataset:
   - Train ID
   - Station
   - Arrival Hour
   - Scheduled Platform
   - Passenger Load
   - Track Availability
   - Weather Score
   - Delay Minutes (target)

2. Trained a RandomForestRegressor model to predict delay.

3. Built optimization module:
   - Dynamic platform load balancing
   - Congestion score calculation based on passenger load and peak traffic

4. Developed an interactive Streamlit dashboard.

## Model Used

Random Forest Regressor

Evaluation Metric:
Mean Absolute Error (MAE)

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib

## How to Run

1. Clone the repository

```
git clone <your-repo-link>
cd smart-rail-planner
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run application

```
streamlit run app.py
```

## Assumptions

- Data is synthetic and generated using probabilistic logic.
- Passenger load and weather affect delays.
- Track unavailability increases delay probability.
- Congestion score is computed using passenger density and peak hour trains.

## Future Improvements

- Real-time schedule integration
- Deep learning-based delay prediction
- Reinforcement learning for dynamic platform assignment
- Multi-station optimization
- Cloud deployment (GCP/AWS)