import numpy as np
from sklearn.linear_model import LinearRegression   # pip install scikit-learn
from sklearn.svm import SVR  
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import GridSearchCV
import pickle

# Raw data
data = [
    (35, 90.0), (15, 87.0), (27, 100.0), (27, 100.0), (2, 84.0), (35, 90.0),
    (33, 104.0), (33, 104.0), (31, 106.0), (30, 101.0), (32, 102.0), (18, 109.0),
    (8, 147.0), (1, 81.0), (10, 134.0), (14, 88.0), (18, 109.0), (22, 107.0),
    (18, 107.0), (3, 76.0), (22, 106.0), (9, 136.0), (32, 103.0), (34, 99.0),
    (6, 50.0), (25, 107.0), (13, 86.0), (23, 109.0), (5, 60.0), (21, 107.0),
    (22, 108.0), (27, 101.0), (1, 82.0), (32, 102.0), (27, 101.0), (35, 95.0),
    (31, 99.0), (18, 119.0), (27, 101.0)
]

# Separate channel_data and azimuth angles
channel_data = np.array([d[0] for d in data]).reshape(-1, 1)
azimuth_angles = np.array([d[1] for d in data])

# Calculate the difference between the target angle (90) and the given azimuth angles
angle_difference = 90 - azimuth_angles

# Scale the channel data
scaler = StandardScaler()
channel_data_scaled = scaler.fit_transform(channel_data)

# Fit the SVR model
model = SVR(kernel='rbf')

#Define the range of hyperparameters for grid search
param_grid = {
    'C': [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],       # 100000000 was the best
    'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]        # gamma 100 was the best
}
# Perform grid search with cross-validation
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(channel_data_scaled, angle_difference)

# Print the best hyperparameters
print(grid_search.best_params_)

# Get the best estimator from the grid search
best_model = grid_search.best_estimator_

# Save the best model and scaler to files
with open('svr_best_model.pkl', 'wb') as file:
    pickle.dump(best_model, file)

with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)

