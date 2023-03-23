import re
import pickle
import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
    channel_data = []
    azimuth_angles = []
    for line in content:
        if "channel_data" in line:
            channel_data.append(int(re.search(r'\d+', line).group()))
        if "Azimuth angle" in line:
            azimuth_angles.append(float(re.search(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', line).group()))
    return channel_data, azimuth_angles

def plot_data(channel_data, azimuth_angles, title, figure_number):
    plt.figure(figure_number)
    plt.scatter(channel_data, azimuth_angles)
    plt.xlabel('channel_data')
    plt.ylabel('Azimuth angle (degrees)')
    plt.title(title)
    plt.grid()

def apply_calibration(channel_data, azimuth_angles, model, poly_features):
    channel_data = np.array(channel_data).reshape(-1, 1)
    channel_data_poly = poly_features.transform(channel_data)
    calibrated_angles = model.predict(channel_data_poly) + azimuth_angles
    return calibrated_angles

if __name__ == '__main__':
    filename = '230323_141930_channel_vs_Azimuth.txt'
    channel_data, azimuth_angles = read_data(filename)
    
    # # Load the Linear Regresiion
    # with open('linear_regression_model.pkl', 'rb') as file:
    #     loaded_model = pickle.load(file)
    
    # Load the model and polynomial features
    with open('poly_regression_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    
    with open('poly_features.pkl', 'rb') as file:
        loaded_poly_features = pickle.load(file)

    calibrated_angles = apply_calibration(channel_data, azimuth_angles, loaded_model, loaded_poly_features)

    plot_data(channel_data, azimuth_angles, 'channel_data vs Azimuth angle (Original)', 1)
    plot_data(channel_data, calibrated_angles, 'channel_data vs Azimuth angle (Calibrated)', 2)
    plt.show()