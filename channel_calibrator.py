import numpy as np
from sklearn.linear_model import LinearRegression   # pip install scikit-learn
from sklearn.preprocessing import PolynomialFeatures
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

# Print angle difference
print('Angle difference:', angle_difference)

#Create polynomial features
degree = 150 # Experiment with different degrees
# min_degree = 199
# max_degree = 199
poly_features = PolynomialFeatures(degree=degree, include_bias=False)
channel_data_poly = poly_features.fit_transform(channel_data)

# Fit the polynomial regression model
model = LinearRegression().fit(channel_data_poly, angle_difference)

# Save the model and polynomial features to files
with open('poly_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('poly_features.pkl', 'wb') as file:
    pickle.dump(poly_features, file)